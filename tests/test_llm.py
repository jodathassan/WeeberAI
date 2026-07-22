from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = client.models.generate_content(
        model="models/gemini-3.6-flash",
        contents=prompt
    )

    print("Gemini:", response.text)