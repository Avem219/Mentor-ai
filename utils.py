import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyBkEJsWUTW1T2QRmOwMXfFWrBFw7uj3CZM"))

def mentor_ai_tutor(question, premium=False, quiz=False):
    try:
        model = genai.GenerativeModel("gemini-pro")

        style = "**Premium Detailed Mode Enabled**\n\n" if premium else ""
        quiz_mode = "\n\nAlso create a short quiz with answers hidden." if quiz else ""

        full_prompt = f"""
You are Mentor AI Tutor, a friendly academic explainer.
Keep explanations clear and student-friendly.

{style}

User question:
{question}

{quiz_mode}
"""

        response = model.generate_content(full_prompt)

        return response.text

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
