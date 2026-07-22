import pandas as pd
from pathlib import Path


def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATA_PATH = (
        BASE_DIR
        / "data"
        / "processed"
        / "cleaned_anime.csv"
    )

    print("Loading processed dataset...")

    df = pd.read_csv(DATA_PATH)


    print("\nDataset Shape:")
    print(df.shape)


    print("\nSynopsis Length Statistics:")
    print(
        df["synopsis"]
        .str.len()
        .describe()
    )


    print("\nAnime with missing/short synopsis:")

    bad_synopsis = df[
        df["synopsis"].str.len() < 50
    ][
        [
            "title",
            "synopsis"
        ]
    ]


    print(
        bad_synopsis.head(20)
    )


    print("\nTotal bad synopsis:")
    print(
        len(bad_synopsis)
    )


if __name__ == "__main__":
    main()