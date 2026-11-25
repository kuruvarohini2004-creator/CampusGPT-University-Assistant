
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key not found in .env")
    raise SystemExit

print("1. API key loaded successfully.", flush=True)

client = genai.Client(api_key=api_key)

print("2. Connecting to Gemini...", flush=True)

try:
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input="Reply with exactly: CampusGPT connection successful.",
        timeout=30
    )

    print("3. Gemini response received:", flush=True)
    print(response.output_text, flush=True)

except Exception as error:
    print("4. Gemini request failed:", flush=True)
    print(type(error).__name__, str(error), flush=True)
