import kaggle
from os import listdir
from os.path import isfile, join

import argparse

def download_df(df: str, usr_name, key):
    if not os.path.exists("data"):
        os.makedirs("data")
    k = kaggle.KaggleApi({"username": usr_name, "key": key})
    k.authenticate()
    print("kaggle.com: authenticated")
    k.dataset_download_cli(df, unzip=True, path="data")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='Kaggle username', type=str)
    parser.add_argument('--key', help='Kaggle access key', type=str)
    parser.add_argument('--df', help='Dataset name from kaggle.com', type=str)
    args = parser.parse_args()
    df_name = args.df
    kaggle_username = args.username
    kaggle_key = args.key
    download_df(df_name, kaggle_username, kaggle_key)

