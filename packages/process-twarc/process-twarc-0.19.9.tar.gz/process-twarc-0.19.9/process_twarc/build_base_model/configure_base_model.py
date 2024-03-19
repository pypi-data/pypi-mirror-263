from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
import torch
import pandas as pd

def process(
        path_to_new_tokenizer: str,
        donor_paths,
        donate_token_embeddings: bool=True,
        donate_cls_embeddings: bool=True,
        push_to_hub: str=""
):
    
    def get_vocab(tokenizer):
        return set(tokenizer.get_vocab().keys())

    def get_tokenizers_and_models(
        donor_paths,
        path_to_new_tokenizer=path_to_new_tokenizer
    ):
        if type(donor_paths) == str:
            donor_paths = [donor_paths]
        
        load_tokenizer = lambda path: AutoTokenizer.from_pretrained(path)
        load_model = lambda path: AutoModel.from_pretrained(path)

        donors = [{path: {
            "tokenizer": load_tokenizer(path),
            "model": load_model(path),
        }} for path in donor_paths]

        for donor in donors:
            donor["vocab"] = get_vocab(donor["tokenizer"])

        new_tokenizer = load_tokenizer(path_to_new_tokenizer)
        new_model = load_model(donor_paths[0])

        return donors, new_tokenizer, new_model
    
    def assign_donors(
        new_tokenizer: str,
        donors, 
        migrate_cls_embeddings=migrate_cls_embeddings
        ):

        def assign_fn(token):
            for name, tok_data in donors.items():
                if token in tok_data["vocab"]:
                    return (name, "token")
            
            if migrate_cls_embeddings:
                for name, tok_data in donors.items():
                    if not "[UNK]" in tok_data["tokenizer"].tokenize(token):
                        return (name, "cls")
            return ("random", None)
        
        vocab = get_vocab(new_tokenizer)
        assignments = [assign_fn(token) for token in vocab]

        donor_df = pd.DataFrame({
            "token": vocab,
            "donor": [a[0] for a in assignments],
            "method": [a[1] for a in assignments]
        })
        return donor_df

    def compare_embeddings(
            old_model,
            new_model,
            old_token_id,
            new_token_id
            ):
        old_embedding = old_model.embeddings.word_embeddings.weight[old_token_id]
        new_embedding = new_model.embeddings.word_embeddings.weight[new_token_id]
        similarity = torch.nn.functional.cosine_similarity(old_embedding, new_embedding, dim=0)
        return similarity.item()

    def migrate_token_embeddings(
            new_tokenizer,
            new_model,
            tokens,
            donor
            ):
        
        donor_tokenizer, donor_model = donor
        token_id_mapping = {}
        with torch.no_grad():
            for token in tqdm(tokens):
                old_token_id = donor_tokenizer.convert_tokens_to_ids(token)
                new_token_id = new_tokenizer.convert_tokens_to_ids(token)
                new_model.embeddings.word_embeddings.weight[new_token_id] = donor_model.embeddings.word_embeddings.weight[old_token_id]
                token_id_mapping[old_token_id] = new_token_id
        threshold = 0.9
        mismatched_tokens = []
        for old_token_id, new_token_id in token_id_mapping.items():
            similarity = compare_embeddings(donor_model, new_model, old_token_id, new_token_id)
            if similarity < threshold:
                mismatched_tokens.append(new_tokenizer.convert_ids_to_tokens(new_token_id))

        if not mismatched_tokens:
            print("All migrated embeddings are similar above the threshold.")
        else:
            print(f"Mismatched tokens: {mismatched_tokens}")
        return new_model

    def migrate_cls_embeddings(
            new_tokenizer,
            new_model,
            tokens,
            donor):
        
        donor_tokenizer, donor_model = donor
        with torch.no_grad():
            for token in tqdm(tokens):
                inputs = donor_tokenizer(token, return_tensors="pt", add_special_tokens=True)
                input_ids = inputs['input_ids']
                attention_mask = inputs['attention_mask']

                ouputs = donor_model(input_ids, attention_mask=attention_mask)
                
                cls_embedding = ouputs.last_hidden_state[:, 0, :]
                new_token_id = new_tokenizer.convert_tokens_to_ids(token)
                new_model.embeddings.word_embeddings.weight[new_token_id] = cls_embedding
        return new_model
    
    donors, new_tokenizer, new_model = get_tokenizers_and_models(donor_paths)
    donor_df = assign_donors(new_tokenizer, donors)
    for group, df in donor_df.groupby(["donor", "method"] ):
        if group[1] == "token" and donate_token_embeddings:
            new_model = migrate_token_embeddings(new_tokenizer, new_model, df["token"], donors[group[0]])
        elif group[1] == "cls" and donate_cls_embeddings:
            new_model = migrate_cls_embeddings(new_tokenizer, new_model, df["token"], donors[group[0]])
    
    new_model.save_pretrained(path_to_new_tokenizer)
    if push_to_hub:
        new_model.push_to_hub(push_to_hub)
        new_tokenizer.push_to_hub(push_to_hub)

    
