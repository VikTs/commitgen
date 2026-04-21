import os
from dotenv import load_dotenv
from groq import Groq
from prompt import build_prompt

load_dotenv()

client = Groq(api_key=os.getenv("AI_API_KEY"))

def ask_to_commit() -> bool:
    answer = input("\nCommit changes? (y/n): ").strip().lower()
    return answer.lower() in ["y", "yes"]

def generate_commit(diff: str) -> str:
    try:
        model = os.getenv("AI_MODEL_NAME")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Generate one git commit message."},
                {"role": "user", "content": build_prompt(diff)}
            ],
            temperature=0.1
        )

        raw = response.choices[0].message.content

        return raw

    except Exception:
        return "chore: update code"