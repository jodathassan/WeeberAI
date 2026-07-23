from google.genai.errors import (
    ClientError,
    ServerError,
)

from app.services.gemini_service import (
    generate_gemini_answer,
)

from app.services.ollama_service import (
    generate_ollama_answer,
)


def generate_answer(prompt: str):
    """
    Generate an answer using Gemini.
    Automatically falls back to Ollama if Gemini fails.

    Returns:
        tuple[str, str]
        (answer, model_used)
    """

    # -----------------------------
    # Try Gemini
    # -----------------------------

    try:

        print("=" * 50)
        print("Using Gemini...")
        print("=" * 50)

        answer = generate_gemini_answer(
            prompt
        )

        return answer, "Gemini"

    # -----------------------------
    # Gemini API errors
    # -----------------------------

    except (ClientError, ServerError) as e:

        print("=" * 50)
        print("Gemini failed.")
        print(e)
        print("Switching to Ollama...")
        print("=" * 50)

    # -----------------------------
    # Unexpected errors
    # -----------------------------

    except Exception as e:

        print("=" * 50)
        print("Unexpected Gemini error.")
        print(e)
        print("Switching to Ollama...")
        print("=" * 50)

    # -----------------------------
    # Ollama fallback
    # -----------------------------

    try:

        answer = generate_ollama_answer(
            prompt
        )

        return answer, "Ollama"

    except Exception as e:

        print("=" * 50)
        print("Ollama also failed.")
        print(e)
        print("=" * 50)

        return (
            "Sorry, both Gemini and the local model are currently unavailable.",
            "None",
        )