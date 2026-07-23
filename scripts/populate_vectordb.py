import os
from pathlib import Path
import urllib.request
import numpy as np
import pandas as pd
from tqdm import tqdm
from app.database.chroma_client import get_collection

BATCH_SIZE = 500

# Direct link to raw binary (if you upload to GitHub Releases or Hugging Face)
# For now, this script checks if the file is an LFS pointer and handles it.

def is_lfs_pointer(file_path: Path) -> bool:
    """Check if the file is a Git LFS pointer text file instead of real binary data."""
    if not file_path.exists():
        return False
    if file_path.stat().st_size < 2000:  # LFS pointers are ~100-200 bytes
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                return "version https://git-lfs.github.com/spec/v1" in content
        except Exception:
            return False
    return False


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    embeddings_file = BASE_DIR / "data" / "embeddings" / "embeddings.npy"
    metadata_file = BASE_DIR / "data" / "embeddings" / "metadata.parquet"

    # 1. Check for Git LFS pointer issue
    if is_lfs_pointer(embeddings_file):
        raise RuntimeError(
            f"'{embeddings_file.name}' is a Git LFS pointer text file (~1 KB) instead of binary data. "
            "Railway did not pull the LFS object during build."
        )

    # 2. Load Embeddings
    try:
        embeddings = np.load(embeddings_file)
    except Exception:
        try:
            embeddings = np.load(embeddings_file, allow_pickle=True)
        except Exception as err:
            raise RuntimeError(f"Failed to load numpy embeddings: {err}")

    # 3. Load Metadata
    metadata = pd.read_parquet(metadata_file)

    collection = get_collection()

    print("Removing existing collection data...")
    try:
        existing_ids = collection.get()["ids"]
        if existing_ids:
            collection.delete(ids=existing_ids)
    except Exception:
        pass

    print("Adding anime to ChromaDB...\n")
    total = len(metadata)

    for start in tqdm(range(0, total, BATCH_SIZE)):
        end = min(start + BATCH_SIZE, total)
        batch_embeddings = embeddings[start:end]
        batch_metadata = metadata.iloc[start:end]

        ids = batch_metadata["anime_id"].astype(str).tolist()
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
    print(f"Total anime: {collection.count()}")
    print("==============================")


if __name__ == "__main__":
    main()