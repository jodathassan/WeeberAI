import shutil
from pathlib import Path
import chromadb
from chromadb.config import Settings

COLLECTION_NAME = "anime_collection"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DIR = BASE_DIR / "data" / "chroma"

_client = None
_collection = None


def get_chroma_client():
    global _client
    if _client is None:
        CHROMA_DIR.mkdir(parents=True, exist_ok=True)
        try:
            _client = chromadb.PersistentClient(
                path=str(CHROMA_DIR),
                settings=Settings(anonymized_telemetry=False, allow_reset=True),
            )
        except Exception as e:
            # If the database file is corrupted (code 26), wipe the folder and start fresh
            print(f"ChromaDB corrupted ({e}). Resetting database directory...")
            if CHROMA_DIR.exists():
                shutil.rmtree(CHROMA_DIR)
            CHROMA_DIR.mkdir(parents=True, exist_ok=True)
            _client = chromadb.PersistentClient(
                path=str(CHROMA_DIR),
                settings=Settings(anonymized_telemetry=False, allow_reset=True),
            )
    return _client


def get_collection():
    global _collection
    if _collection is None:
        client = get_chroma_client()
        _collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"description": "Anime Recommendation Collection"},
        )
    return _collection