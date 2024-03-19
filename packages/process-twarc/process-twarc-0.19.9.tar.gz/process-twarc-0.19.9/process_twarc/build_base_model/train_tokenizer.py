from process_twarc.util import (
    concat_dataset,
    get_files,
    make_dir,
    load_dict,
    get_output_path
)
import fugashi
import unidic_lite
from process_twarc.build_base_model.pre_tokenize import pre_tokenize_pipeline
from process_twarc.build_base_model.build_training_corpus import generate_low_freq_char_mask
from tokenizers import (
    models,
    pre_tokenizers,
    trainers,
    Tokenizer
    )
from transformers import BertJapaneseTokenizer
import os
from ntpath import basename


def build_tokenizer(
        training_corpus_dir: str,
        vocab_dir: str,
        tokenizer_dir: str,
        push_to_hub= "",
        vocab_size: int=32000,
        mask_low_freq_char: bool=True,
        standard_special_tokens = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
        additional_special_tokens = ["[URL]", "[USER]"],
        keep_newlines: bool=True,
        hashtags_masked: bool=True
):
    def get_training_corpus(dataset):
        for i in range(0, len(dataset), 1000):
            yield dataset[i : i + 1000]["pre_tokenized"]
    
    def get_vocab():
        masks = "low_freq_char" if mask_low_freq_char else None

        dataset = concat_dataset(
            get_files(training_corpus_dir),
            output_type="Dataset",
            columns="pre_tokenized",
            masks=masks
        )
        trainer_special_tokens = standard_special_tokens + additional_special_tokens
        if keep_newlines:
            trainer_special_tokens = trainer_special_tokens + "\n"
        if hashtags_masked:
            trainer_special_tokens = trainer_special_tokens + "#"

        tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
        tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
        trainer = trainers.WordPieceTrainer(vocab_size=vocab_size, special_tokens=trainer_special_tokens)

        tokenizer.train_from_iterator(get_training_corpus(dataset), trainer=trainer)
        
        make_dir(vocab_dir)
        tokenizer_name = basename(training_corpus_dir)
        path_to_vocab_json = os.path.join(vocab_dir, f"{tokenizer_name}".json)
        tokenizer.save(path_to_vocab_json)
        return path_to_vocab_json, tokenizer_name
    
    def generate_sorted_vocab_list():
        path_to_vocab_json, tokenizer_name = get_vocab()
        vocab = list(load_dict(path_to_vocab_json).keys())
        vocab = [word for word in vocab if word != "\n"]
        length = lambda token: len(token.replace("##", ""))
        sort_key = lambda token: (length(token), token.startswith("##"), token)

        special_tokens = standard_special_tokens + additional_special_tokens
        non_special = [word for word in vocab if word not in special_tokens]
        non_special.sort(key=sort_key)
        sorted_vocab = special_tokens + non_special

        vocab_file = get_output_path(path_to_vocab_json, vocab_dir, file_type = "txt")
        with open(vocab_file, "w", encoding="utf-8") as f:
            f.write("\n".join(sorted_vocab))
        return vocab_file, tokenizer_name

    def configure_tokenizer():
        vocab_file, tokenizer_name = generate_sorted_vocab_list()
        tokenizer = BertJapaneseTokenizer(
            vocab_file=vocab_file,
            word_tokenizer_type="mecab",
            mecab_kwargs={"mecab_dic": "unidic_lite"},
            keep_newlines=keep_newlines,
            model_max_length=512,
            additional_special_tokens=additional_special_tokens
        )
        if keep_newlines:
            tokenizer.add_tokens("\n")
        if additional_special_tokens:
            tokenizer.additional_special_tokens=additional_special_tokens
        
        path_to_tokenizer = os.path.join(tokenizer_dir, tokenizer_name)
        tokenizer.save_pretrained(path_to_tokenizer)
        if push_to_hub:
            tokenizer.push_to_hub(push_to_hub)
    
    configure_tokenizer()

def train_tokenizer_pipeline(
        data_dir: str,
        pre_tokenized_dir: str,
        training_corpus_dir: str,
        vocab_dir: str,
        tokenizer_dir: str,
        mask_low_freq_char: bool=True,
        vocab_size: int=32_000,
        standard_special_tokens: list = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
        additional_special_tokens: list = ["[URL]", "[USER]"],
        keep_newlines: bool=True,
        push_to_hub: str="",
        pre_tokenizer: object=fugashi.Tagger('-d "{}"'.format(unidic_lite.DICDIR)),
        hashtags_masked: bool=True
):
    pre_tokenize_pipeline(
        data_dir=data_dir,
        pre_tokenized_dir=pre_tokenized_dir,
        pre_tokenizer=pre_tokenizer
    )

    if mask_low_freq_char:
        generate_low_freq_char_mask(
            training_corpus_dir=training_corpus_dir
        )

    build_tokenizer(
        training_corpus_dir=training_corpus_dir,
        vocab_dir=vocab_dir,
        tokenizer_dir=tokenizer_dir,
        push_to_hub=push_to_hub,
        vocab_size=vocab_size,
        mask_low_freq_char=mask_low_freq_char,
        standard_special_tokens=standard_special_tokens,
        additional_special_tokens=additional_special_tokens,
        keep_newlines=keep_newlines,
        hashtags_masked=hashtags_masked 
    )
