from groq import Groq
from django.conf import settings

SYSTEM_PROMPT = """You are an expert electrical engineer specializing in 
electrical machines. Answer questions clearly about motors, generators, 
transformers, and drives. Keep answers to 3-4 paragraphs, beginner-friendly.
If the question is unrelated to electrical machines, politely say so."""


def get_ai_answer(question_text):
    api_key = settings.GROQ_API_KEY

    if not api_key:
        return "Groq API key not configured. Add GROQ_API_KEY to your .env file."

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question_text},
            ],
            max_tokens=600,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error fetching answer: {str(e)}"