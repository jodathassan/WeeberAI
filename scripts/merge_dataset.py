from pathlib import Path
import pandas as pd

def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    SYNOPSIS_FILE = (
        BASE_DIR /
        "data" /
        "raw" /
        "anime_with_synopsis.csv"
    )

    ANIME_FILE = (
        BASE_DIR /
        "data" /
        "raw" /
        "anime.csv"
    )

    OUTPUT_FILE = (
        BASE_DIR /
        "data" /
        "processed" /
        "merged_anime.csv"
    )

    print("Loading datasets...")

    synopsis_df = pd.read_csv(
        SYNOPSIS_FILE
    )

    anime_df = pd.read_csv(
        ANIME_FILE
    )

    print("Synopsis dataset:")
    print(synopsis_df.head())

    print("\nAnime dataset:")
    print(anime_df.head())

    # Rename columns for merging

    synopsis_df.rename(
        columns={
            "MAL_ID": "anime_id",
            "Name": "title",
            "Genres": "genre",
            "sypnopsis": "synopsis"
        },
        inplace=True
    )

    anime_df.rename(
        columns={
            "MAL_ID": "anime_id"
        },
        inplace=True
    )

    # Merge

    merged = synopsis_df.merge(
        anime_df,
        on="anime_id",
        how="left"
    )

    print("\nMerged shape:")
    print(merged.shape)

    # Keep useful columns

    columns = [
        "anime_id",
        "title",
        "English name",
        "genre",
        "synopsis",
        "Score",
        "Type",
        "Episodes",
        "Studios",
        "Rating"
    ]

    # Keep only columns that exist

    columns = [
        col for col in columns
        if col in merged.columns
    ]

    merged = merged[columns]

    # Rename nicely

    merged.rename(
        columns={
            "English name": "title_english",
            "Score": "score",
            "Type": "type",
            "Episodes": "episodes",
            "Studios": "studio",
            "Rating": "rating"
        },
        inplace=True
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    merged.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n==========================")
    print("Merge completed!")
    print("==========================")
    print(
        f"Saved: {OUTPUT_FILE}"
    )

if __name__ == "__main__":
    main()