
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: Groq API key not found!")
    raise SystemExit

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: CampusGPT connection successful."
            }
        ],
        max_completion_tokens=100
    )

    print(response.choices[0].message.content)

except Exception as error:
    print("Groq API Error:", error)
