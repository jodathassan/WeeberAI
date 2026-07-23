# Weeber - AI Anime Recommendation System

Weeber is a full-stack AI-powered anime recommendation system that combines **Retrieval-Augmented Generation (RAG)** with a **Large Language Model (Google Gemini)** to provide intelligent anime recommendations and answer anime-related questions.

Unlike traditional recommendation systems, Weeber retrieves semantically relevant anime using vector search and then uses an LLM to generate natural, context-aware responses.

---

## Features

### AI Chatbot

- Conversational anime assistant
- Natural language understanding
- Recommendation mode
- Information mode

### Retrieval-Augmented Generation (RAG)

- Sentence Transformers embeddings
- ChromaDB vector database
- Semantic similarity search
- Context-aware prompting

### Intelligent Recommendation Engine

- Detects recommendation intent
- Detects information queries
- Removes duplicate recommendations
- Filters sequels, OVAs, movies and specials
- Ranking based on similarity

### LLM Integration

- Google Gemini
- Automatic fallback support (Ollama ready)
- Hallucination-reduced prompting

### Frontend

- Next.js 16
- React 19
- TypeScript
- Tailwind CSS
- Framer Motion animations
- Modern ChatGPT-inspired interface

### Backend

- FastAPI
- Pydantic
- REST API
- Modular architecture

---

# Tech Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion

## Backend

- FastAPI
- Pydantic

## AI

- Google Gemini
- Sentence Transformers
- ChromaDB

---

# Project Structure

```
AnimeRecommendation(LLM + RAG)

│
├── app/
│   ├── api/
│   ├── database/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── public/
│
├── data/
│
├── scripts/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/weeber.git

cd weeber
```

---

## Backend

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend

Move into frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Create

```
frontend/.env.local
```

Add

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:3000
```

---

# API Endpoint

POST

```
/recommend
```

Request

```json
{
  "query": "Recommend anime like Death Note"
}
```

---

# Example Queries

- Recommend anime like Naruto
- Best psychological anime
- Recommend dark fantasy anime
- What is One Piece about?
- Recommend romance anime
- Explain Attack on Titan

---

# Future Improvements

- User accounts
- Chat history
- Streaming responses
- Anime posters
- MAL integration
- Personalized recommendations
- Hybrid retrieval
- Deployment on Render + Vercel

---

# Author

**Syed Jodat Hassan Naqvi**

BS Software Engineering

GitHub:
https://github.com/jodathassan