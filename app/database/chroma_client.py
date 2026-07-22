from pathlib import Path
import chromadb
from chromadb.config import Settings

# Collection name
COLLECTION_NAME = "anime_collection"

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Chroma persistence directory
CHROMA_DIR = BASE_DIR / "data" / "chroma"


def get_chroma_client():
    """
    Returns a persistent ChromaDB client.
    """

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR),
        settings=Settings(anonymized_telemetry=False),
    )

    return client


def get_collection():

    client = get_chroma_client()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={
            "description": "Anime Recommendation Collection"
        },
    )

    return collection