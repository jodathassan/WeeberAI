from typing import List

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    query: str = Field(
        ...,
        min_length=1,
        examples=["Recommend anime like Death Note"],
    )


class AnimeSource(BaseModel):

    title: str

    genre: str

    score: float

    similarity: float


class ChatResponse(BaseModel):

    intent: str

    model: str | None

    answer: str

    sources: List[AnimeSource]