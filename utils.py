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
        # Quota / billing / access issue handling
        if "quota" in str(e).lower():
            return "⚠️ Your AI usage limit has been reached. Please wait for reset or upgrade."
        elif "model" in str(e).lower():
            return "⚠️ Model not available on your account. Try gpt-3.5-turbo."
        else:
            return f"⚠️ Error: {str(e)}"
