
import pandas as pd
from process_twarc.util import  get_output_path, save_to_parquet, load_dataset, concat_dataset, get_files
import re
from datasets import Dataset
from torch.utils.data import DataLoader
def get_file_type(file_path):
    """
    Get the file type from the file path.

    Args:
        file_path (str): The file path.

    Returns:
        str: The file type.
    """
    return file_path.split(".")[-1]

def process_twarc_file(file_path: str, output_dir: str=""):
    """
    Process a file acquired from Twarc2 and generate a parquet file with columns: tweet_id, text.

    Args:
        file_path (str): Path to the input file.
        output_dir (str): Directory where the generated parquet file will be saved.
    """
    file_type = get_file_type(file_path)

    if file_type == "jsonl":
        df = pd.read_json(file_path, lines=True, encoding="utf-8")
    elif file_type == "json" or file_type == "txt":
        df = pd.read_json(file_path, encoding="utf-8")
    else:
        raise ValueError("Unsupported file type: {}".format(file_type))

    if file_type == "txt":
        tweet_ids = df["id"].astype(str).tolist()
        author_ids = df["author_id"].astype(str).tolist()
        texts = df["text"].tolist()
    else:
        tweet_ids = []
        texts = []
        author_ids = []

        for data in df["data"]:
            for item in data:
                tweet_ids.append(str(item["id"]))
                author_ids.append(str(item["author_id"]))
                texts.append(item["text"])

    new_df = pd.DataFrame({
        "tweet_id": tweet_ids,
        "author_id": author_ids,
        "text": texts})

    if output_dir:
        output_path = get_output_path(file_path, output_dir, file_type="parquet")
        save_to_parquet(new_df, output_path)
    return new_df

def add_special_tokens(text: str):
    """
    Replaces URLs and usernames in the given text with special tokens.

    Args:
        text (str): The input text.

    Returns:
        str: The text with replaced URLs and usernames.
    """
    text = re.sub("https://t[^ ]+", "[URL]", text)
    text = re.sub("@[^ ]+", "[USER]", text)
    return text

def generate_masks(file_path, duplicate_text, output_dir:str="", duplicates=True, characters=True, patterns=True):
    """
    Generates masks based on various conditions for a given dataset.

    Args:
        file_path (str): Path to the dataset file.
        duplicate_text (Set[str]): Set of duplicate texts to check against.
        output_dir (str): Directory to save the output.

    Returns:
        pd.DataFrame: Processed dataset with added mask columns.

    """
    def check_duplicate(example:str, duplicate_text:set):
        """Checks if the text has been flagged as duplicate."""
        return example in duplicate_text
 
    def check_pattern(example:str):
        """Check if the text has one of the frequently occuring patterns defined below."""
        patterns = [
            "\AI('m| was) at.*in.*",
            "\(@ .*in.*\)"
            ]
        return any(re.search(pattern, example) for pattern in patterns)

    masked_dataset = load_dataset(file_path)
    masked_dataset["low_freq_char"], masked_dataset["duplicate"], masked_dataset["pattern"] = False, False, False
    for idx, row in masked_dataset.iterrows():
        text = row["text"]
        tokenized = row["tokenized"]
        masked_dataset.at[idx, "duplicate"] = check_duplicate(tokenized, duplicate_text)
        masked_dataset.at[idx, "pattern"] = check_pattern(text)
    
    masked_dataset = masked_dataset.remove_columns("tokenized")
    
    if output_dir:
        output_path = get_output_path(file_path, output_dir)
        save_to_parquet(masked_dataset, output_path)
    return masked_dataset


def tokenize_for_masked_language_modeling(
        dataset: Dataset, 
        tokenizer: object, 
        path_to_output: str=""
        ):
    """
    The final step in preprocessing the data for masked language modeling.

    Duplicate rows are removed, and the text is tokenized.

    Afterwards, the tokenized text is filtered to remove examples that are too long.

    Args:
        file_path (str): Path to the dataset.
        path_to_tokenizer (str): Path to the tokenizer.
        output_dir (str): Directory to save the output.

    Returns:
        pd.DataFrame: Tokenized dataset.
    """
    def tokenize(example):
        return tokenizer.encode_plus(example["text"], max_length=280, truncation=True)
    
    tokenized_dataset = dataset.map(tokenize, remove_columns="text")
    tokenized_dataset = tokenized_dataset.filter(lambda example: len(example["input_ids"])<=117)

    if path_to_output:
        save_to_parquet(tokenized_dataset, path_to_output)
    return tokenized_dataset

def generate_splits(
        raw_datasets,
        output_dir: str="",
        seed: int=42,
        test_size: float=0.1,
        validation_size: float= 0.05,
        development_size: float=0.1,
        print_details: bool=True):
    
    """
    The native train_test_split function from HuggingFace's Datasets library is limited in that it will only split the dataset into two parts.

    This function add the options to split into "validation" and "development" sets.

    Args:
        data_dir (str): Path to the dataset.
        seed (int, optional): Random seed for the split.
        test_size (float, optional): Size of the test set.
        validation_size (float, optional): Size of the validation set.
        development_size (float, optional): Size of the development set.
        print_details (bool, optional): Whether to print the details of the split.

    """
    print("Splitting datasets. . .")

    if isinstance(raw_datasets, pd.DataFrame):
        raw_datasets = Dataset.from_pandas(raw_datasets)
    split_size = test_size + validation_size + development_size
    splits = raw_datasets.train_test_split(test_size = split_size, seed = seed)
    if validation_size:
        split = splits.pop("test")
        test_size = test_size/split_size
        validation_size = validation_size/split_size
        development_size = development_size/split_size
        split_size = test_size + development_size

        split_dataset = split.train_test_split(train_size = validation_size, test_size=split_size, seed = seed)
        splits["validation"], splits["test"] = split_dataset["train"], split_dataset["test"]

    if development_size:
        split = splits.pop("test")
        test_size = test_size/split_size
        development_size = development_size/split_size

        split_dataset = split.train_test_split(train_size=development_size, test_size=test_size, seed=seed)
        splits["development"], splits["test"] = split_dataset["train"], split_dataset["test"]

    if print_details:
        print(splits)

    if output_dir:
        for split in splits.keys():
            print ("Saving", split)
            path_to_output = f"{output_dir}/{split}.parquet"
            save_to_parquet(splits[split], path_to_output)
    return splits
