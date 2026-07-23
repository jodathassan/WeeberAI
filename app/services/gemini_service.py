from google import genai
from google.genai.errors import ClientError, ServerError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from app.config import GOOGLE_API_KEY, GEMINI_MODEL


client = genai.Client(
    api_key=GOOGLE_API_KEY
)


@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    retry=retry_if_exception_type((ServerError, ClientError)),
    reraise=True,
)
def generate_gemini_answer(prompt: str) -> str:
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text