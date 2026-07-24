import os
from groq import Groq

def generate_groq_answer(prompt: str) -> str:
    """
    Generate an answer using Groq's fast cloud Llama-3.1 model.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is missing.")

    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Extremely fast, free cloud model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return completion.choices[0].message.content