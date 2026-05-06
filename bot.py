import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQKEY")
if not api_key:
    raise ValueError("GROQKEY is missing. Check your .env file.")

client = Groq(api_key=api_key)

with open("data.txt", "r", encoding="utf-8") as f:
    context = f.read()


def ask_bot(question: str) -> str:
    try:
        messages = [
            {
                "role": "system",
                "content": f"""
You are a personal AI assistant for Jayamurugan B.

Verified information:
{context}

Rules:
* Answer only questions related to Jayamurugan B.
* Be clear, professional, and short
* If unrelated, politely refuse
"""
            },
            {"role": "user", "content": question}
        ]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages  
        )

        return response.choices[0].message.content  

    except Exception as e:  
        print("ERROR:", e)
        return str(e)