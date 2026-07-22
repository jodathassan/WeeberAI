from sentence_transformers import SentenceTransformer
from app.database.chroma_client import get_collection


MODEL_NAME = "all-MiniLM-L6-v2"


model = SentenceTransformer(
    MODEL_NAME
)


BAD_TITLE_WORDS = [
    "season",
    "movie",
    "special",
    "ova",
    "ona",
    "recap",
    "chronicle",
    "collab",
    "trailer",
    "pv",
    "promotion",
    "short",
    "summary"
]


def is_bad_recommendation(title: str):

    title = title.lower()

    for word in BAD_TITLE_WORDS:
        if word in title:
            return True

    return False



def retrieve_anime(
        query: str,
        top_k: int = 8,
        recommendation=False
):


    collection = get_collection()



    if recommendation:

        search_query = f"""

Find anime recommendations for this user request:

{query}


Do NOT find the exact same anime.

Instead find anime with similar:

- story themes
- emotional impact
- atmosphere
- character development
- conflicts
- audience


Prioritize:

- dark fantasy
- psychological thriller
- military conflict
- survival
- war
- strategy
- morally complex characters
- serious storytelling


Return standalone anime.
Avoid:
- sequels
- movies
- specials
- recap episodes
- promotional content

"""


    else:

        search_query = query



    embedding = model.encode(
        search_query,
        normalize_embeddings=True
    )



    # retrieve more because we will filter
    results = collection.query(

        query_embeddings=[
            embedding.tolist()
        ],

        n_results=50

    )



    anime_results = []



    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]



    for metadata, distance in zip(
        metadatas,
        distances
    ):


        title = metadata.get(
            "title",
            "Unknown"
        )



        similarity = round(
            1 - distance,
            3
        )



        # Remove weak matches
        if similarity < 0.35:
            continue



        # Remove bad recommendation results
        if recommendation and is_bad_recommendation(title):
            continue



        score = metadata.get(
            "score",
            0
        )


        try:
            score = float(score)

        except:
            score = 0



        anime_results.append(

            {

                "title": title,


                "genre": metadata.get(
                    "genre",
                    ""
                ),


                "score": score,


                "synopsis": metadata.get(
                    "synopsis",
                    ""
                ),


                "similarity": similarity,


                # ranking score
                "ranking_score": (
                    similarity * 0.8
                    +
                    (score / 10) * 0.2
                )

            }

        )



    # Better ranking:
    # similarity + popularity/quality

    anime_results.sort(
        key=lambda x: x["ranking_score"],
        reverse=True
    )


    return anime_results[:8]