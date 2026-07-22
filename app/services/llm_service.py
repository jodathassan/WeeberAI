import os
from google import genai
from google.genai.errors import ServerError, ClientError
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Catch both 503 (Server Overload) and 429 (Rate Limit / Quota Exceeded)
@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    retry=retry_if_exception_type((ServerError, ClientError)),
    reraise=True
)
def generate_answer(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Higher daily quota (250 RPD vs 20 RPD)
        contents=prompt
    )

    return response.text