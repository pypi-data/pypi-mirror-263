from transformers import AutoTokenizer, TrainerCallback, Trainer, get_constant_schedule_with_warmup, get_linear_schedule_with_warmup, get_cosine_schedule_with_warmup, get_cosine_with_hard_restarts_schedule_with_warmup, DataCollatorWithPadding, DataCollatorForLanguageModeling, TrainingArguments, EarlyStoppingCallback, AutoModelForMaskedLM, AutoModelForSequenceClassification
from process_twarc.util import load_dataset, load_dict
import torch
from torch.optim import AdamW
import wandb
import optuna
from ntpath import basename
import evaluate
import numpy as np
import os
import shutil


def login_to_wandb(path_to_keys: str="keys/keys.json"):
    key = load_dict(path_to_keys)["wandb_api_key"]
    wandb.login(key=key)
    return

class OptunaCallback(TrainerCallback):
    def __init__(self, trial, should_prune):
        self.trial = trial
        self.should_prune = should_prune

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        eval_loss = metrics.get("eval_loss")
        self.trial.report(eval_loss, step=state.global_step)
        if self.should_prune and self.trial.should_prune():
            raise optuna.TrialPruned()
        
class StopCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, logs=None, **kwargs):
        control.should_training_stop = True
        control.should_save = True

class DualLearningRateTrainer(Trainer):
    def __init__(self, *args, pretrained_token_indices: list=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.pretrained_token_indices = pretrained_token_indices
        self.reduced_lr_factor = self.args.reduced_lr_factor

    def _get_current_lr(self):
        # Retrieve the current learning rate from the optimizer
        return self.optimizer.param_groups[0]["lr"]
    
    def training_step(self, model, inputs):
        model.train()
        inputs = self._prepare_inputs(inputs)

        loss = self.compute_loss(model, inputs)
        if self.args.gradient_accumulation_steps > 1:
            loss = loss / self.args.gradient_accumulation_steps
        
        loss.backward()

        if "word_embeddings" in model.base_model.named_parameters():
            word_embeddings = model.base_model.get_input_embeddings()
            if self.pretrained_token_indices:
                word_embeddings.weight.grad[self.pretrained_token_indices] *= self.reduced_lr_factor
            
        if "wandb" in self.args.report_to:
            lr = self._get_current_lr()
            reduced_lr = lr * self.reduced_lr_factor
            wandb.log({"learning_rate": lr, "reduced_learning_rate": reduced_lr})

        return loss.detach()
    
class CustomTrainingArguments(TrainingArguments):
    def __init__(self, *args, reduced_lr_factor=None, wandb_run_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if reduced_lr_factor:
            self.reduced_lr_factor = reduced_lr_factor
        if wandb_run_id:
            self.wandb_run_id = wandb_run_id

def get_compute_metrics(parameters):
    argmax_ = lambda x: np.argmax(x, axis=1)

    metrics = parameters["metrics"]
    metrics = [metrics] if type(metrics) == str else metrics
    if "accuracy" in metrics:
        def compute_accuracy(eval_pred):
            accuracy = evaluate.load("accuracy")
            predictions, labels = eval_pred
            if parameters["label_type"] == "hard":  
                predictions = argmax_(predictions)
            elif parameters["label_type"] == "soft":
                predictions, labels = argmax_(predictions), argmax_(labels)
            return accuracy.compute(predictions=predictions, references=labels)
        return compute_accuracy

def load_datasets(
        data_dir: str,
        splits: list=["train", "validation", "development"],
        preprocessed_data: bool=False,
        label_column: str="",
        tokenizer: object=None):
    
    def load_(split, label_column: str=""):
        path = os.path.join(data_dir, f"{split}.parquet")
        if preprocessed_data:
            dataset = load_dataset(path, output_type="Dataset")
        else:
            columns = ["text"]
            if label_column:
                columns.append(label_column)
            dataset = load_dataset(path, output_type="Dataset", columns=columns)
            if tokenizer:
                dataset = dataset.map(lambda example: tokenizer(example["text"]), batched=True)
            if label_column not in ["", "label"]:
                dataset = dataset.rename_column(
                    original_column_name=label_column,
                    new_column_name= "label")
        return dataset

    tokenized_datasets = {split: load_(split, label_column) for split in splits}

    return tokenized_datasets

def get_study_name(config, group: str=None):
    if group:
        study_name = group
    else:
        study_name = config["fixed_parameters"]["group"]
    return study_name

def get_sampler(config):
    variable_parameters = config["variable_parameters"]

    search_type = variable_parameters["search_type"]
    if search_type == "TPE":
        sampler = optuna.samplers.TPESampler()
    if search_type == "random":
        sampler = optuna.samplers.RandomSampler()
    if search_type == "grid":
    
        search_field = variable_parameters["search_field"]
        def get_choices(parameter):
            param = search_field[parameter]
            type_ = search_field[parameter]["type"]
            if type_ in ["int", "float"]:
                start = param["low"]
                stop = param["high"] + param["step"]
                step = param["step"]
                choices = list(np.arange(start, stop, step))
            elif type_ == "categorical":
                choices = param["choices"]   
            return choices
        
        search_field = {k:get_choices(k) for k in search_field.keys()}
        sampler = optuna.samplers.GridSampler(search_field)
    return sampler

def get_model(model_class, parameters, tokenizer):
    if model_class == AutoModelForSequenceClassification:
        model = model_class.from_pretrained(
            parameters["path_to_model"],
            num_labels=parameters["num_labels"],
            id2label=parameters["id2label"],
            label2id=parameters["label2id"]
        )
        collator_class = DataCollatorWithPadding

    elif model_class == AutoModelForMaskedLM:
        model = model_class.from_pretrained(
            parameters["path_to_model"]
            )
        collator_class = DataCollatorForLanguageModeling

    data_collator = collator_class(tokenizer=tokenizer)
    return model, data_collator


def get_optimizer(model, parameters, optimizer_state: str=None):
    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    optimizer = AdamW(
        params=model.parameters(),
        lr=get("learning_rate"),
        betas = (get("adam_beta1"), get("adam_beta2")),
        eps = get("adam_epsilon"),
        weight_decay = get("weight_decay")
    )
    
    if optimizer_state:
        optimizer.load_state_dict(optimizer_state)

    return optimizer


def get_scheduler(train_dataset, parameters, optimizer, scheduler_state: str=None):

    get = lambda parameter, default: parameters[parameter] if parameter in parameters.keys() else default

    lr_scheduler_type = get("lr_scheduler_type", "constant")
    batch_size = get("per_device_train_batch_size", 15)
    num_train_epochs = get("num_train_epochs", 1)
    num_cycles = get("num_cycles", 0.5)
    num_restarts = get("num_restarts", 0)
    warmup_steps = get("warmup_steps", 0)
    inverse_warmup_ratio = get("inverse_warmup_ratio", 0.0)

    num_training_steps = len(train_dataset) // batch_size * num_train_epochs
    if inverse_warmup_ratio:
        warmup_steps = num_training_steps // inverse_warmup_ratio
        parameters["warmup_steps"] = warmup_steps


    if lr_scheduler_type == "constant":
        scheduler = get_constant_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=warmup_steps
        )
    elif lr_scheduler_type == "linear":
        scheduler = get_linear_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps= num_training_steps
        )
    
    elif lr_scheduler_type == "cosine":
        scheduler = get_cosine_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps= num_training_steps,
            num_cycles=num_cycles
        )
    elif lr_scheduler_type == "cosine_with_restarts":
        scheduler = get_cosine_with_hard_restarts_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps= num_training_steps,
            num_cycles=num_restarts
        )
    if scheduler_state:
        scheduler.load_state_dict(scheduler_state)

    return scheduler, parameters

def get_optimizers(model, parameters, train_dataset, last_checkpoint: str=""):
    optimizer_state, scheduler_state = None, None
    if last_checkpoint:
        optimizer_state = torch.load(os.path.join(last_checkpoint, "optimizer.pt"))
        scheduler_state = torch.load(os.path.join(last_checkpoint, "scheduler.pt"))

    optimizer = get_optimizer(model, parameters, optimizer_state)
    scheduler, parameters = get_scheduler(train_dataset, parameters, optimizer, scheduler_state)
    return (optimizer, scheduler), parameters

def get_current_epoch(last_checkpoint):
    return load_dict(os.path.join(last_checkpoint, "trainer_state.json"))["epoch"]

def get_paths(trial, parameters):
    join = lambda parent, child: os.path.join(parent, child)
    start = parameters["trial_number_start"] if "trial_number_start" in parameters.keys() else 1
    trial_number = str(trial.number+start).zfill(3)
    
    run_name = f"{parameters['group']}/trial-{trial_number}"
    dir_path = f"{parameters['project']}/{run_name}"

    paths = {
        "run_name": run_name,
        "trial_checkpoint": join(parameters["checkpoint_dir"], dir_path),
        "trial_complete": join(parameters["completed_dir"], dir_path)
    }
    return paths

def retrieve_paths(trial_checkpoint, config):
    join = lambda parent, child: os.path.join(parent, child)
    parent = lambda path: os.path.dirname(path)

    parameters = config["fixed_parameters"]

    trial_name = basename(trial_checkpoint)
    group = basename(parent(trial_checkpoint))
    project = basename(parent(parent(trial_checkpoint)))


    run_name = f"{group}/{trial_name}"
    run_path = f"{project}/{run_name}"

    paths = {
        "run_name": run_name,
        "trial_checkpoint": trial_checkpoint,
        "trial_complete": join(parameters["completed_dir"], run_path),
        "last_checkpoint": get_last_checkpoint(trial_checkpoint)
    }
    return paths


def get_callbacks(parameters, pause_on_epoch: bool=False, trial=None, should_prune: bool=False, current_epoch: float=0.0):
    choices = parameters["callbacks"]

    callbacks = []
    if "early_stopping" in choices:
        patience = parameters["patience"]
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=patience))
        print(f"EarlyStopping enabled. {patience=}")
    
    if "optuna" in choices:
        callbacks.append(OptunaCallback(trial, should_prune=should_prune))
        print(f"Optuna logging enabled. {should_prune=}")

    stop_epoch = parameters["num_train_epochs"]
    if pause_on_epoch:
        stop_epoch = int(current_epoch) + 1
        if stop_epoch< parameters["num_train_epochs"]:
            callbacks.append(StopCallback())
            print(f"Training will pause when epoch = {stop_epoch}.")
        else:
            print("Training will run to completion.")
    
    return callbacks, stop_epoch


def configure_dropout(model, config, parameters):
    dropout_parameters = [key for key in parameters.keys() if "dropout" in key]
    if not dropout_parameters:
        return model, config, parameters
    else:
        get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
        def update(model, name, value): 
            model.config.update({name: value})
            parameters[name] = value
            return model, config, parameters

        for dropout in ["hidden_dropout_prob", "attention_probs_dropout_prob", "classifier_dropout"]:
            model, config, parameters = update(model, dropout, get(dropout))

        fixed_parameters, variable_parameters = config["fixed_parameters"], config["variable_parameters"]["search_field"]
        listify = lambda parameter: parameter if type(parameter) == list else [parameter]
        dropout_type = get("dropout_type")
        choice=None


        if "dropout_type" in fixed_parameters.keys():
            choice = listify(dropout_type)

        elif "dropout_type" in variable_parameters.keys():
            if dropout_type:
                label2choice = variable_parameters["dropout_type"]["label2choice"]
                choice = listify(label2choice[dropout_type])

        if choice:
            if "hidden" in choice:
                model, config, parameters = update(model, "hidden_dropout_prob", get("dropout_prob"))
            if "attention" in choice:
                model, config, parameters = update(model, "attention_probs_dropout_prob", get("dropout_prob"))
            if "classifier" in choice:
                model, config, parameters = update(model, "classifier_dropout", get("dropout_prob"))
                
        else:
            model, config, parameters = update(model, "dropout_prob", None)
    return model, config, parameters


def configure_training_args(
        parameters,
        paths,
):
    if "interval" in parameters.keys():
        evaluation_strategy = save_strategy = "steps"
        eval_steps = save_steps = 1 / parameters["interval"] / parameters["num_train_epochs"]
    else:
        evaluation_strategy = save_strategy = "epoch"
        eval_steps = save_steps = 1

    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    training_args = CustomTrainingArguments(
        adam_beta1=get("adam_beta1"),
        adam_beta2=get("adam_beta2"),
        adam_epsilon=get("adam_epsilon"),
        eval_steps=eval_steps,
        evaluation_strategy=evaluation_strategy,
        logging_steps=get("logging_steps"),
        learning_rate=get("learning_rate"),
        load_best_model_at_end=get("load_best_model_at_end"),
        lr_scheduler_type=get("lr_scheduler_type"),
        metric_for_best_model=get("metric_for_best_model"),
        num_train_epochs=get("num_train_epochs"),
        output_dir=paths["trial_checkpoint"],
        per_device_train_batch_size=get("per_device_train_batch_size"),
        per_device_eval_batch_size=get("per_device_eval_batch_size"),
        push_to_hub=get("push_to_hub"),
        reduced_lr_factor=get("reduced_lr_factor"),
        report_to=get("report_to"),
        save_strategy=save_strategy,
        save_steps=save_steps,
        save_total_limit=get("patience") if get("patience") != 1 else 2,
        wandb_run_id=get("wandb_run_id"),
        weight_decay=get("weight_decay")
        )
    if get("inverse_warmup_ratio"):
        training_args.warmup_ratio = 1/get("inverse_warmup_ratio")
    elif get("warmup_steps"):
        training_args.warmup_steps = get("warmup_steps")
    
    return training_args


def suggest_parameter(trial, search_space, param_name):

            param_space = search_space[param_name]
            dtype = param_space["type"]
            if dtype == "fixed":
                return param_space["value"]
            elif dtype == "categorical":
                return trial.suggest_categorical(
                    name=param_name,
                    choices=param_space["choices"])
            elif dtype == "int":
                suggest_method = trial.suggest_int
            elif dtype == "float":
                suggest_method = trial.suggest_float
            else:
                raise ValueError("Please input a valid parameter type. Either 'fixed', 'categorical', 'int' or 'float'.")
            if "step" in param_space.keys():
                    return suggest_method(
                        name=param_name,
                        low=param_space["low"],
                        high=param_space["high"],
                        step=param_space["step"]
                    )
            elif "log" in param_space.keys():
                return suggest_method(
                    name=param_name,
                    low=param_space["low"],
                    high=param_space["high"],
                    log=param_space["log"]
                )
            else:
                return suggest_method(
                    name=param_name,
                    low=param_space["low"],
                    high=param_space["high"]
                )

def compile_parameters(search_space, trial):
    param_names = [name for name in search_space.keys() if name != "meta"]
    parameters = {name: suggest_parameter(trial, search_space, name) for name in param_names}
    return parameters

def init_parameters(trial, config, override_parameters={}, group: str=None):
    fixed_parameters = config["fixed_parameters"]
    if group:
        group_parameters = config["group_parameters"][group]
        group_parameters["group"] = group
    else:
        group_parameters = {}


    search_field = config["variable_parameters"]["search_field"]
    
    suggest = lambda variable: suggest_parameter(trial, search_field, variable)
    variable_parameters = {variable: suggest(variable) for variable in search_field.keys()}

    parameters = {**fixed_parameters, **group_parameters, **variable_parameters, **override_parameters}
    return parameters

def init_wandb(parameters, paths, reinit: bool=False):
    trial_checkpoint, run_name = paths["trial_checkpoint"], paths["run_name"]
    project, group, entity = parameters["project"], parameters["group"], parameters["entity"]
    

    if not reinit:
        os.makedirs(trial_checkpoint, exist_ok=True)
        wandb_run_id = wandb.util.generate_id()
        parameters["wandb_run_id"] = wandb_run_id

        wandb.init(
            project=project,
            id=parameters["wandb_run_id"],
            dir=trial_checkpoint,
            group=group,
            entity=entity,
            name=run_name,
            resume="allow",
            config=parameters,
            reinit=True
        )

    else:
        wandb_run_id = parameters["wandb_run_id"]

        wandb.init(
            project= project,
            id=wandb_run_id,
            resume="must"
            )
    return parameters

def print_parameters(config, parameters, pretrained_token_indices: list=[]):
    
    print("\nFixed Params:")
    for key, value in config["fixed_parameters"].items():
        print(f"{key}: {value}")

    if "group_parameters" in config.keys():
        print("\nGroup Params:")
        groups = list(config["group_parameters"].keys())
        for key in config["group_parameters"][groups[0]].keys():
            print(f"{key}: {parameters[key]}")

    print("\nVariable Params:")
    for key in config["variable_parameters"]["search_field"].keys():
        if key in parameters.keys():
            print(f"{key}: {parameters[key]}")
    
    if "reduced_lr_factor" in parameters.keys():
        print("Daul Learning Rate Enabled")
        print(f"Reduced Learning Rate Factor: {parameters['reduced_lr_factor']}")
        print(f"Total Pretrained Tokens: {len(pretrained_token_indices)}")
    return

def print_run_init(model, config, parameters, paths, pretrained_token_indices: list=[], reinit: bool=False):
    print("\n", model.config)
    print_parameters(config, parameters, pretrained_token_indices=pretrained_token_indices)

    if not reinit:
        print(f"Beginning {basename(paths['trial_checkpoint'])}. . .")

    else:
        print(f"Resuming {basename(paths['trial_checkpoint'])}. . .")
    return

def get_trainer(
        model,
        args,
        data_collator,
        datasets,
        tokenizer,
        compute_metrics,
        optimizers,
        callbacks,
        parameters,
        pretrained_token_indices: list=[],
):
    trainer_args = {
        "model": model,
        "args": args,
        "data_collator": data_collator,
        "train_dataset": datasets["train"],
        "eval_dataset": datasets["validation"],
        "tokenizer": tokenizer,
        "compute_metrics": compute_metrics,
        "optimizers": optimizers,
        "callbacks": callbacks
    }
    if "reduced_lr_factor" in parameters.keys():
        trainer_args["pretrained_token_indices"] = pretrained_token_indices
        trainer = DualLearningRateTrainer(**trainer_args)
    else:
        trainer = Trainer(**trainer_args)
    return trainer
     

def init_run(
        trial, 
        config: dict, 
        model_class: object,
        datasets: dict,
        tokenizer,
        pretrained_token_indices: list=[],
        group: str="", 
        override_parameters: dict={}, 
        pause_on_epoch: bool=False, 
        should_prune: bool=False):
    
    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")
    parameters = init_parameters(
        trial, 
        config,
        override_parameters=override_parameters, 
        group=group)
    paths = get_paths(trial, parameters)
    model, data_collator = get_model(model_class, parameters, tokenizer)
    model, config, parameters = configure_dropout(model, config, parameters)
    model.to(device)

    if parameters["report_to"] == "wandb":
        parameters = init_wandb(parameters, paths)

    training_args = configure_training_args(parameters, paths)
    optimizers, parameters = get_optimizers(model, parameters, datasets["train"])
    if parameters["warmup_steps"]:
        training_args.warmup_steps = parameters["warmup_steps"]
    
    compute_metrics = get_compute_metrics(parameters)

    callbacks, stop_epoch = get_callbacks(
        parameters, 
        pause_on_epoch=pause_on_epoch,
        trial=trial,
        should_prune=should_prune)

    trainer = get_trainer(
        model,
        training_args,
        data_collator,
        datasets,
        tokenizer,
        compute_metrics,
        optimizers,
        callbacks,
        parameters,
        pretrained_token_indices=pretrained_token_indices
    )

    print_run_init(
        model, 
        config, 
        parameters,
        paths,
        pretrained_token_indices=pretrained_token_indices)
    
    return parameters, paths, trainer, stop_epoch

def get_last_checkpoint(trial_checkpoint: str):

    checkpoints = [os.path.join(trial_checkpoint, checkpoint) for checkpoint in os.listdir(trial_checkpoint) if os.path.isdir(os.path.join(trial_checkpoint, checkpoint))]
    return max(checkpoints, key=os.path.getctime)

def retrieve_parameters(trial_checkpoint, config, model_class, override_parameters={}):

    paths= retrieve_paths(trial_checkpoint, config)
    get = lambda target: os.path.join(paths["last_checkpoint"], target)
    training_args = torch.load(get("training_args.bin"))
    training_args_dict = {k:v for k,v in training_args.__dict__.items() if k != "callbacks"}

    model_config = load_dict(get("config.json"))
    parameters = {**training_args_dict, **model_config, **config["fixed_parameters"], **override_parameters}
    tokenizer = AutoTokenizer.from_pretrained(parameters["path_to_model"])

    model, data_collator = get_model(model_class, parameters, tokenizer)
    model.config.update(model_config)

    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")
    model.to(device)
    return paths, training_args, parameters, tokenizer, model, data_collator

def reinit_run(
        trial_checkpoint, 
        config, 
        model_class,
        data_dir,
        pretrained_token_indices: list=[],
        override_parameters: dict={},
        preprocessed_data: bool=True,
        pause_on_epoch: bool=False
        ):

    paths, training_args, parameters, tokenizer, model, data_collator = retrieve_parameters(
        trial_checkpoint, 
        config,
        model_class,
        override_parameters=override_parameters)

    datasets = load_datasets(
        data_dir,
        preprocessed_data=preprocessed_data,
        label_column=parameters["label_column"] if "label_column" in parameters.keys() else "",
        tokenizer=tokenizer if not preprocessed_data else None
        )   
    
    
    optimizers, parameters = get_optimizers(model, parameters, datasets["train"], paths["last_checkpoint"])
    callbacks, stop_epoch = get_callbacks(
        parameters,
        pause_on_epoch=pause_on_epoch,
        current_epoch=get_current_epoch(paths["last_checkpoint"]),
    )

    compute_metrics = get_compute_metrics(parameters)

    if parameters["report_to"] == "wandb":
        init_wandb(parameters, paths, reinit=True)

    trainer = get_trainer(
        model,
        training_args,
        data_collator,
        datasets,
        tokenizer,
        compute_metrics,
        optimizers,
        callbacks,
        parameters,
        pretrained_token_indices=pretrained_token_indices
    )

    print_run_init(
        model,
        config,
        parameters,
        paths,
        pretrained_token_indices=pretrained_token_indices,
        reinit=True
    ) 
    return paths, parameters, datasets, trainer, stop_epoch

def check_if_complete(trainer, parameters, stop_epoch):
    def early_stopping_triggered():
        if "early_stopping" in parameters["callbacks"]:
            return trainer.state.epoch < stop_epoch
        else:
            return False
        
    current_epoch = trainer.state.epoch
    if early_stopping_triggered():
        print("EarlyStoppingCallback triggered.")
        complete = True

    elif current_epoch == parameters["num_train_epochs"]:
        print("Training complete.")
        complete = True
    else:
        complete = False
        print(f"Training paused. {current_epoch=}.")
    return complete

def complete_trial (
        trainer, 
        datasets, 
        parameters, 
        paths
        ):
    
    trial_checkpoint, trial_complete = paths["trial_checkpoint"], paths["trial_complete"]
    if "development" in datasets.keys():
        test_dataset = datasets["development"]
    else:
        test_dataset = datasets["test"]

    results = trainer.evaluate(test_dataset)
    print("\nResults:", results)
    trainer.save_model(trial_complete)
    if parameters["report_to"] == "wandb":
        wandb.log(results)
        wandb.finish()
        #move wandb directory to completed directory
        wandb_dir = os.path.join(trial_checkpoint, "wandb")
        shutil.move(wandb_dir, trial_complete)
    #deletes the trial directory
    shutil.rmtree(trial_checkpoint)

    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    if get("metric_for_best_trial"):
        trial_value = results[get("metric_for_best_trial")]
    elif get("metric_for_best_model"):
        trial_value = results[get("metric_for_best_model")]
    else:
        trial_value = results["eval_loss"] 
    return trial_value

def launch_study(
        config, 
        path_to_storage, 
        data_dir, 
        preprocessed_data,
        override_parameters: dict={},  
        group: str=""):

    if group:
        parameters = {**config["fixed_parameters"], **config["group_parameters"][group], **{"group": group}}
    else:
        parameters = config["fixed_parameters"]
    
    if override_parameters:
        parameters = {**parameters, **override_parameters}
    
    if parameters["metric_for_best_trial"] in ["accuracy", "eval_accuracy"]:
        direction = "maximize"

    elif parameters["metric_for_best_trial"] in ["loss", "eval_loss"]:
        direction = "minimize"

    tokenizer = AutoTokenizer.from_pretrained(parameters["path_to_model"], print_details=False)

    get = lambda parameter: parameters[parameter] if parameter in parameters.keys() else None
    datasets = load_datasets(
        data_dir,
        preprocessed_data=preprocessed_data,
        label_column = get("label_column"),
        tokenizer=tokenizer
        )

    study = optuna.create_study(
        storage=path_to_storage,
        sampler=get_sampler(config),
        study_name=parameters["group"],
        direction=direction,
        load_if_exists=True,
        )
    
    return tokenizer, datasets, study