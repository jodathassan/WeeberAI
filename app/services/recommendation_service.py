from app.services.intent_service import detect_intent
from app.services.prompt_builder import build_prompt
from app.services.retrieval_service import (
    retrieve_information,
    retrieve_recommendations,
)
from app.services.llm_service import generate_answer


def recommend(user_query: str):

    intent = detect_intent(user_query)

    print(f"Detected intent: {intent}")

    # -----------------------------
    # Retrieve context
    # -----------------------------

    if intent == "recommendation":

        anime_context = retrieve_recommendations(
            user_query
        )

    else:

        anime_context = retrieve_information(
            user_query
        )

    # -----------------------------
    # Nothing retrieved
    # -----------------------------

    if len(anime_context) == 0:

        return {

            "intent": intent,

            "model": None,

            "answer": (
                "Sorry, I couldn't find any relevant anime "
                "in my database."
            ),

            "sources": []

        }

    # -----------------------------
    # Build prompt
    # -----------------------------

    prompt = build_prompt(

        query=user_query,

        anime_results=anime_context,

        intent=intent

    )

    # -----------------------------
    # Generate answer
    # -----------------------------

    answer, model_used = generate_answer(
        prompt
    )

    # -----------------------------
    # Return response
    # -----------------------------

    return {

        "intent": intent,

        "model": model_used,

        "answer": answer,

        "sources": anime_context

    }