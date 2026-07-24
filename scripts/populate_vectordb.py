from pathlib import Path
import urllib.request
from app.database.chroma_client import get_collection
import numpy as np
import pandas as pd
from tqdm import tqdm

BATCH_SIZE = 500

# Direct raw download URL for GitHub LFS file
LFS_URL = "https://github.com/jodathassan/WeeberAI/raw/main/data/embeddings/embeddings.npy"


def is_lfs_pointer(file_path: Path) -> bool:
  """Check if file is missing or a Git LFS pointer text file."""
  if not file_path.exists():
    return True
  if file_path.stat().st_size < 2000:
    try:
      with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return "version https://git-lfs.github.com/spec/v1" in f.read()
    except Exception:
      return False
  return False


def main():
  BASE_DIR = Path(__file__).resolve().parent.parent
  embeddings_file = BASE_DIR / "data" / "embeddings" / "embeddings.npy"
  metadata_file = BASE_DIR / "data" / "embeddings" / "metadata.parquet"

  collection = get_collection()

  # Skip if already populated
  if collection.count() > 0:
    print(f"Database already contains {collection.count()} items. Skipping.")
    return

  # Auto-download binary directly if Railway pulled a 1 KB text pointer
  if is_lfs_pointer(embeddings_file):
    print("LFS pointer detected. Downloading full binary embeddings file...")
    embeddings_file.parent.mkdir(parents=True, exist_ok=True)

    req = urllib.request.Request(
        LFS_URL,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    )
    with (
        urllib.request.urlopen(req) as response,
        open(embeddings_file, "wb") as out_file,
    ):
      out_file.write(response.read())

    print("Download finished!")

  # Load Embeddings
  try:
    embeddings = np.load(embeddings_file)
  except Exception:
    embeddings = np.load(embeddings_file, allow_pickle=True)

  # Load Metadata
  metadata = pd.read_parquet(metadata_file)

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
      metadatas.append({
          "title": row["title"],
          "title_english": row["title_english"],
          "genre": row["genre"],
          "episodes": int(row["episodes"]),
          "studio": row["studio"],
          "type": row["type"],
          "rating": row["rating"],
          "synopsis": row["synopsis"],
      })

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