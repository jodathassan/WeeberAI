import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

input_file = (
    BASE_DIR /
    "data" /
    "processed" /
    "cleaned_anime.csv"
)


output_file = (
    BASE_DIR /
    "data" /
    "processed" /
    "final_anime.csv"
)


df = pd.read_csv(input_file)


# Remove extremely short synopsis
df = df[
    df["synopsis"].str.len() > 50
]


df.reset_index(drop=True, inplace=True)


df.to_csv(
    output_file,
    index=False
)


print("Finished")
print("Remaining anime:", len(df))