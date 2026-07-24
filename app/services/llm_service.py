from app.services.gemini_service import generate_gemini_answer
from app.services.groq_service import generate_groq_answer


def generate_answer(prompt: str):
    """
    Tries Gemini first. If Gemini fails (or hits quota limits),
    automatically falls back to Groq.
    """

    # 1. Try Gemini
    try:
        print("Using Gemini...")
        answer = generate_gemini_answer(prompt)
        return answer, "Gemini"
    except Exception as e:
        print(f"Gemini failed ({e}). Switching to Groq...")

    # 2. Try Groq (Fallback)
    try:
        print("Using Groq...")
        answer = generate_groq_answer(prompt)
        return answer, "Groq"
    except Exception as e:
        print(f"Groq failed as well ({e}).")
        return (
            "Sorry, both Gemini and Groq are currently unavailable.",
            "None",
        )