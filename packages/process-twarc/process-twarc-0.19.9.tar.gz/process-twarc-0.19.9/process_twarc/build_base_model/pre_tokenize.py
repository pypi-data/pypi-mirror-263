import unicodedata
from process_twarc.util import make_dir, load_dataset, get_files, save_to_parquet, get_output_path
from tqdm import tqdm
import fugashi
import unidic_lite
import re
from datasets import Dataset

"""
The HuggingFace tokenizer trainer is designed to work with space segmented text.
To use it with Japanese text, the text must be pre-tokenized.

This pipeline normalizes the text, removes tags, and pretokenizes the text using fugashi and unidic_lite.

In this process, character sets are also generated for each tweet. This will be used to determine
"""

def pretokenize_dataset(
        file: str,
        pre_tokenized_dir: str = "",
        tokenizer = fugashi.Tagger('-d "{}"'.format(unidic_lite.DICDIR))

        ) -> Dataset:
    """
    Prepares the text for building a corpus for training a tokenizer.
    
    Args:
        file (str): The file to process
        pre_tokenized_dir (str): The directory to save the pre-tokenized data
        tokenizer (fugashi.Tagger): The tokenizer to use
    
    Returns:
        Dataset: The pre-tokenized dataset with the following columns:
            "tweet_id": The tweet id
            "text": The original text
            "hashtags_masked": The text with hashtags masked
            "user_cap": Bool with True if the tweet is to be masked when Users are capped.
            "normalized": The normalized text
            "charset": The character set of the normalized text
            "cleaned_text": The normalized text with tags removed
            "pre_tokenized": The cleaned text, pre_tokenized by fugashi
    """
    
    # Normalizes by same method as the HuggingFace BertJapaneseTokenizer
    def normalize_fn(text):
       return unicodedata.normalize("NFKC", text)

    # Compresses the normalized text to a set of unique characters
    def charset_fn(normalized):
        return list(set(normalized))
    
    # Removes tags from the normalized text
    def clean_fn(normalized):
        return re.sub(r"\[(URL|USER|HASHTAG)\]", "", normalized)
    
    # Tokenizes the cleaned text using fugashi
    def tokenize_fn(cleaned_text):
        return " ".join([word.surface for word in tokenizer(cleaned_text)])
    
    
    make_dir(pre_tokenized_dir)
    dataset = load_dataset(
        file,
        output_type = "Dataset",
        columns = ["tweet_id", "text", "hashtags_masked", "user_cap"],
        masks = ["duplicate", "pattern"]
        )
    
    dataset = dataset.map(lambda x: {"normalized": normalize_fn(x["text"])}, desc="Normalizing. . .")
    dataset = dataset.map(lambda x: {"charset": charset_fn(x["normalized"])}, desc="Generating character sets. . .")
    dataset = dataset.map(lambda x: {"cleaned_text": clean_fn(x["normalized"])}, desc="Cleaning tags from text. . .")
    dataset = dataset.map(lambda x: {"pre_tokenized": tokenize_fn(x["cleaned_text"])}, desc="Pre-tokenizing text. . .")

    if pre_tokenized_dir:
        output_path = get_output_path(file, pre_tokenized_dir)
        save_to_parquet(dataset, output_path)
    return dataset

def pre_tokenize_pipeline(
    data_dir: str,
    pre_tokenized_dir: str,
    tokenizer = fugashi.Tagger('-d "{}"'.format(unidic_lite.DICDIR))
    ):
    """Given an input and an output directory, pre-tokenizes the datasets."""
    for file in tqdm(get_files(data_dir), desc="Pre-tokenizing datasets"):
        pretokenize_dataset(
            file, 
            pre_tokenized_dir,
            tokenizer=tokenizer)