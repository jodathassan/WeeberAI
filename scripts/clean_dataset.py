from pathlib import Path
import pandas as pd

def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    INPUT_FILE = (
        BASE_DIR /
        "data" /
        "processed" /
        "merged_anime.csv"
    )

    OUTPUT_FILE = (
        BASE_DIR /
        "data" /
        "processed" /
        "final_anime.csv"
    )

    print("Loading dataset...")

    df = pd.read_csv(INPUT_FILE)

    print("Original shape:", df.shape)

    # Keep useful columns

    columns = [
        "anime_id",
        "title",
        "title_english",
        "genre",
        "synopsis",
        "type",
        "episodes",
        "studio",
        "rating"
    ]

    df = df[columns]

    # Fill missing values

    text_columns = [
        "title",
        "title_english",
        "genre",
        "synopsis",
        "type",
        "studio",
        "rating"
    ]

    for col in text_columns:

        df[col] = (
            df[col]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    df["episodes"] = (
        pd.to_numeric(
            df["episodes"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
    )

    # Remove bad synopsis

    df = df[
        df["synopsis"].str.len() > 50
    ]

    # Remove duplicates

    df.drop_duplicates(
        subset=["anime_id"],
        inplace=True
    )

    df.reset_index(
        drop=True,
        inplace=True
    )

    # Create RAG document

    df["document"] = (

        "Title: "
        + df["title"]

        + "\nEnglish Title: "
        + df["title_english"]

        + "\nGenres: "
        + df["genre"]

        + "\nType: "
        + df["type"]

        + "\nEpisodes: "
        + df["episodes"].astype(str)

        + "\nStudio: "
        + df["studio"]

        + "\nRating: "
        + df["rating"]

        + "\nSynopsis: "
        + df["synopsis"]

    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n==========================")
    print("Cleaning completed")
    print("==========================")
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print("Saved:", OUTPUT_FILE)

if __name__ == "__main__":
    main()