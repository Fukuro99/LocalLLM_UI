from openai import OpenAI

from .settings import get_settings


settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_note_suggestion(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You help users by drafting concise note ideas.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=120,
        temperature=0.7,
    )

    message = response.choices[0].message.content if response.choices else ""
    return (message or "").strip()
