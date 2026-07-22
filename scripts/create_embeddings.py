from pathlib import Path
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Configuration

MODEL_NAME = "all-MiniLM-L6-v2"
BATCH_SIZE = 128

def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    # Use final dataset after synopsis filtering
    INPUT_FILE = (
        BASE_DIR /
        "data" /
        "processed" /
        "final_anime.csv"
    )

    OUTPUT_DIR = (
        BASE_DIR /
        "data" /
        "embeddings"
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    EMBEDDINGS_FILE = OUTPUT_DIR / "embeddings.npy"

    METADATA_FILE = OUTPUT_DIR / "metadata.parquet"

    print("Loading dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Dataset size: {df.shape}")

    # Safety check
    if "document" not in df.columns:
        raise Exception(
            "document column missing. Run clean_dataset.py again."
        )

    documents = df["document"].fillna("").tolist()

    print(
        f"Loading embedding model ({MODEL_NAME})..."
    )

    model = SentenceTransformer(MODEL_NAME)

    print(
        f"\nGenerating embeddings for {len(documents)} anime...\n"
    )

    embeddings = model.encode(
        documents,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    embeddings = embeddings.astype(
        np.float32
    )

    # Save vectors

    np.save(
        EMBEDDINGS_FILE,
        embeddings
    )

    # Save metadata for ChromaDB

    metadata = df.copy()

    metadata.to_parquet(
        METADATA_FILE,
        index=False
    )

    print("\n====================================")
    print("Embedding generation completed!")
    print("====================================")

    print(
        f"Embeddings shape : {embeddings.shape}"
    )

    print(
        f"Embeddings saved : {EMBEDDINGS_FILE}"
    )

    print(
        f"Metadata saved   : {METADATA_FILE}"
    )

if __name__ == "__main__":
    main()