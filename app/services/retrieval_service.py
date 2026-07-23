import re
from sentence_transformers import SentenceTransformer
from app.database.chroma_client import get_collection

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


BAD_WORDS = {
    "season",
    "movie",
    "special",
    "ova",
    "ona",
    "recap",
    "chronicle",
    "promotion",
    "pv",
    "collab",
    "short",
    "summary",
    "preview"
}


def is_bad_title(title: str) -> bool:
    title = title.lower()
    return any(word in title for word in BAD_WORDS)


def search(query: str, top_k: int = 20):

    collection = get_collection()

    embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=top_k
    )

    anime = []

    for metadata, distance in zip(
        results["metadatas"][0],
        results["distances"][0]
    ):

        try:
            score = float(metadata.get("score", 0))
        except:
            score = 0

        anime.append({

            "title": metadata.get("title", ""),

            "genre": metadata.get("genre", ""),

            "score": score,

            "synopsis": metadata.get("synopsis", ""),

            "similarity": round(
                1 - distance,
                3
            )

        })

    return anime


# ----------------------------------------------------
# INFORMATION RETRIEVAL
# ----------------------------------------------------

def retrieve_information(query: str):

    candidates = search(
        query,
        top_k=15
    )

    query_lower = query.lower()

    exact = []
    others = []

    for anime in candidates:

        title = anime["title"].lower()

        if title == query_lower:
            exact.append(anime)

        elif query_lower in title:
            exact.append(anime)

        else:
            others.append(anime)

    others.sort(
        key=lambda x: (
            x["similarity"],
            x["score"]
        ),
        reverse=True
    )

    return (exact + others)[:5]


# ----------------------------------------------------
# RECOMMENDATION
# ----------------------------------------------------

def extract_reference_title(query: str):

    query = query.lower()

    patterns = [

        r"like (.+)",

        r"similar to (.+)",

        r"after (.+)",

        r"after watching (.+)",

        r"recommend anime like (.+)",

        r"anime similar to (.+)"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            query
        )

        if match:
            return match.group(1).strip()

    return query


def retrieve_recommendations(query: str):

    reference = extract_reference_title(query)

    original = retrieve_information(reference)

    if len(original) == 0:
        return []

    original = original[0]

    similarity_query = f"""
Genre:
{original['genre']}

Synopsis:
{original['synopsis']}

Recommend anime with similar:

- themes
- atmosphere
- pacing
- storytelling
- emotional impact
- character development
"""

    candidates = search(
        similarity_query,
        top_k=50
    )

    recommendations = []

    seen = set()

    original_title = original["title"].lower()

    original_words = set(
        original_title.split()
    )

    for anime in candidates:

        title = anime["title"]

        title_lower = title.lower()

        if title_lower == original_title:
            continue

        if is_bad_title(title):
            continue

        words = set(title_lower.split())

        if len(
            words.intersection(original_words)
        ) >= 2:
            continue

        if title_lower in seen:
            continue

        seen.add(title_lower)

        anime["ranking"] = (

            anime["similarity"] * 0.75

            +

            (anime["score"] / 10) * 0.25

        )

        recommendations.append(anime)

    recommendations.sort(
        key=lambda x: x["ranking"],
        reverse=True
    )

    return recommendations[:8]