from pathlib import Path
import chromadb
from chromadb.config import Settings

# Collection name
COLLECTION_NAME = "anime_collection"

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Chroma persistence directory
CHROMA_DIR = BASE_DIR / "data" / "chroma"

# Cache client and collection to avoid re-initializing on every request
_client = None
_collection = None


def get_chroma_client():
    """
    Returns a singleton persistent ChromaDB client.
    """
    global _client
    if _client is None:
        CHROMA_DIR.mkdir(parents=True, exist_ok=True)
        _client = chromadb.PersistentClient(
            path=str(CHROMA_DIR),
            settings=Settings(anonymized_telemetry=False),
        )
    return _client


def get_collection():
    """
    Returns the cached ChromaDB collection instance.
    """
    global _collection
    if _collection is None:
        client = get_chroma_client()
        _collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={
                "description": "Anime Recommendation Collection"
            },
        )
    return _collection