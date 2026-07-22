from app.services.retrieval_service import retrieve_anime
from app.services.prompt_builder import build_prompt
from app.services.llm_service import generate_answer
from app.services.intent_service import detect_intent


def recommend(user_query: str):


    intent = detect_intent(
        user_query
    )


    print(
        f"Detected intent: {intent}"
    )


    if intent == "recommendation":

        anime_context = retrieve_anime(
            user_query,
            top_k=25,
            recommendation=True
        )


    else:

        anime_context = retrieve_anime(
            user_query,
            top_k=5,
            recommendation=False
        )


    prompt = build_prompt(
        user_query,
        anime_context,
        intent
    )


    answer = generate_answer(
        prompt
    )


    return {

        "answer": answer,

        "sources": anime_context

    }