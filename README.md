# Anime Recommendation System (LLM + RAG)

An AI-powered anime recommendation system built using Retrieval-Augmented Generation (RAG).

## Features

- Semantic search with Sentence Transformers
- ChromaDB vector database
- Gemini API integration
- Intent detection (information vs recommendation)
- Context-aware anime recommendations
- Cleaned anime dataset with synopsis and metadata

## Tech Stack

- Python
- Sentence Transformers
- ChromaDB
- Google Gemini API
- Pandas

## Project Structure

```
app/
scripts/
data/
chroma_db/
```

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run:

```bash
python scripts/test_rag.py
```

## Future Improvements

- FastAPI backend
- Next.js frontend
- Ollama fallback
- Vercel deployment