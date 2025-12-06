from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

def mentor_ai_tutor(question, premium=False, quiz=False):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Mentor AI Tutor."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message["content"]

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def save_progress(user, question, answer):
    pass  # placeholder to avoid import crash


def init_db():
    pass  # placeholder
