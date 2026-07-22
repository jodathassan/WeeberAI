from pathlib import Path
import numpy as np
import pandas as pd
from tqdm import tqdm
from app.database.chroma_client import get_collection

BATCH_SIZE = 500

def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    embeddings = np.load(
        BASE_DIR /
        "data" /
        "embeddings" /
        "embeddings.npy"
    )

    metadata = pd.read_parquet(
        BASE_DIR /
        "data" /
        "embeddings" /
        "metadata.parquet"
    )

    collection = get_collection()

    print("Removing existing collection data...")

    try:
        existing_ids = collection.get()["ids"]

        if existing_ids:
            collection.delete(
                ids=existing_ids
            )

    except Exception:
        pass

    print("Adding anime to ChromaDB...\n")

    total = len(metadata)

    for start in tqdm(range(0, total, BATCH_SIZE)):

        end = min(
            start + BATCH_SIZE,
            total
        )

        batch_embeddings = embeddings[start:end]

        batch_metadata = metadata.iloc[start:end]

        ids = (
            batch_metadata["anime_id"]
            .astype(str)
            .tolist()
        )

        documents = []

        metadatas = []

        for _, row in batch_metadata.iterrows():
            documents.append(row["document"])

            metadatas.append(
                {
                    "title": row["title"],
                    "title_english": row["title_english"],
                    "genre": row["genre"],
                    "episodes": int(row["episodes"]),
                    "studio": row["studio"],
                    "type": row["type"],
                    "rating": row["rating"],
                    "synopsis": row["synopsis"]
                }
            )

        collection.add(
            ids=ids,
            embeddings=batch_embeddings.tolist(),
            documents=documents,
            metadatas=metadatas,
        )

    print("\n==============================")
    print("Vector database created!")
    print("==============================")

    print(
        f"Total anime: {collection.count()}"
    )

if __name__ == "__main__":
    main()