# Weeber - AI Anime Assistant

Weeber is a full-stack AI-powered anime assistant that uses **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)** to answer anime-related questions, provide recommendations, and have natural conversations about anime.

Unlike traditional anime recommendation systems, Weeber does not rely on a custom-trained recommendation model. Instead, it combines **semantic search, vector databases, and LLM reasoning** to retrieve relevant anime information and generate intelligent, context-aware responses.

---

# Features

## AI Anime Chatbot

- Conversational anime assistant
- Natural language understanding
- Answers anime-related questions
- Provides personalized anime recommendations
- Explains anime plots, genres, studios, and details
- Supports recommendation and information queries

---

## Retrieval-Augmented Generation (RAG)

Weeber uses a RAG pipeline to improve response quality:

- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic similarity search
- Context retrieval from anime knowledge base
- LLM-powered response generation

The system retrieves relevant anime information from the vector database and provides that context to the LLM before generating a response.

---

## Intelligent Query Processing

- Detects user intent:
  - Recommendation queries
  - Information queries
- Retrieves relevant anime using vector similarity
- Removes duplicate results
- Filters irrelevant entries:
  - Sequels
  - OVAs
  - Movies
  - Specials
- Generates natural conversational responses

---

## LLM Integration

- Google Gemini API
- Context-aware prompting
- Hallucination-reduced responses
- Ollama support ready for local LLM deployment

---

# System Architecture

Weeber follows a Retrieval-Augmented Generation architecture:

```
                 User Query
                     |
                     v
             Next.js Frontend
                     |
                     v
              FastAPI Backend
                     |
                     v
             Intent Detection
                     |
                     v
        Sentence Transformer Embeddings
                     |
                     v
             ChromaDB Vector Search
                     |
                     v
          Retrieved Anime Information
                     |
                     v
              Google Gemini LLM
                     |
                     v
              Final AI Response
```

The retrieval layer provides relevant anime knowledge to the LLM, allowing Weeber to generate more accurate and meaningful responses.

---

# Tech Stack

## Frontend

- Next.js 16
- React 19
- TypeScript
- Tailwind CSS
- Framer Motion

---

## Backend

- FastAPI
- Python
- Pydantic
- REST API

---

## AI / Machine Learning

- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- Text Embeddings
- Vector Similarity Search
- ChromaDB

---

# Project Structure

```
Weeber
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── database/
│   │   └── chroma_client.py
│   │
│   ├── services/
│   │   ├── recommendation_service.py
│   │   ├── retrieval_service.py
│   │   └── llm_service.py
│   │
│   └── main.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── public/
│
├── data/
│   ├── chroma/
│   └── embeddings/
│
├── scripts/
│
├── requirements.txt
└── README.md
```

---

# Dataset

Weeber uses anime metadata containing:

- Anime titles
- English titles
- Genres
- Studios
- Episodes
- Ratings
- Synopsis

The data is converted into vector embeddings and stored in ChromaDB for semantic retrieval.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/jodathassan/WeeberAI.git

cd WeeberAI
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Never commit API keys or environment files to GitHub.

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# Frontend Setup

Move into frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create:

```
frontend/.env.local
```

Add:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Run:

```bash
npm run dev
```

Frontend:

```
http://localhost:3000
```

---

# API Documentation

## Chat Endpoint

### POST

```
/recommend
```

Request:

```json
{
  "query": "Recommend anime like Attack on Titan"
}
```

Response:

```json
{
  "intent": "recommendation",
  "model": "gemini",
  "answer": "You may enjoy Vinland Saga and Code Geass...",
  "sources": [
    {
      "title": "Vinland Saga",
      "genre": "Action, Adventure",
      "score": 8.7
    }
  ]
}
```

---

# Example Queries

Ask Weeber:

```
Recommend anime like Attack on Titan
```

```
Explain Death Note
```

```
Best psychological anime
```

```
Recommend romance anime
```

```
What is One Piece about?
```

```
Suggest dark fantasy anime
```

---

# Deployment

## Backend

Deployed using:

- Railway

## Frontend

Deployed using:

- Vercel

Environment variables:

Backend:

```env
GOOGLE_API_KEY=your_key
```

Frontend:

```env
NEXT_PUBLIC_API_URL=backend_url
```

---

# Future Improvements

- User accounts
- Chat history
- Streaming responses
- Anime posters and images
- MyAnimeList integration
- Personalized user preferences
- Hybrid retrieval system
- Voice-based anime assistant
- Multi-language support

---

# Author

**Syed Jodat Hassan Naqvi**

BS Software Engineering

GitHub:

https://github.com/jodathassan