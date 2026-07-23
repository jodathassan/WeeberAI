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
        "http://localhost:3000",
        "https://weeber-ai.vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    try:
        collection = get_collection()
        print(f"Current collection count: {collection.count()}")
    except Exception as e:
        print(f"Error during startup vector DB check: {e}")


@app.get("/seed")
def seed_database():
    """Manually trigger vector database population and see exact logs/errors."""
    try:
        from scripts.populate_vectordb import main as populate_db
        populate_db()
        collection = get_collection()
        return {
            "status": "success",
            "message": f"Database populated successfully! Total items: {collection.count()}"
        }
    except Exception as e:
        return {
            "status": "error",
            "detail": str(e)
        }


@app.get("/")
def root():
    return {
        "message": "Welcome to Weeber API!",
        "docs": "/docs"
    }