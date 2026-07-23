from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database.chroma_client import get_collection


app = FastAPI(
    title="Weeber API",
    description="Anime Recommendation System using RAG + Gemini + Ollama",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",          # Next.js local dev
        "https://weeber-ai.vercel.app",   # Vercel production
        "*"                               # Optional: Allows all origins for easy testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    """
    Runs automatically when the FastAPI server starts.
    If ChromaDB is empty on Railway, it populates the vector database.
    """
    try:
        collection = get_collection()
        if collection.count() == 0:
            print("Vector database is empty! Populating ChromaDB on startup...")
            from scripts.populate_vectordb import main as populate_db
            populate_db()
            print("Vector database populated successfully!")
        else:
            print(f"Vector database loaded with {collection.count()} items.")
    except Exception as e:
        print(f"Error during startup vector DB check: {e}")


@app.get("/")
def root():
    return {
        "message": "Welcome to Weeber API!",
        "docs": "/docs"
    }