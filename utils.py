import openai
import sqlite3
import os

# --- OpenAI client using Streamlit secret ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# --- Database functions ---
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, premium INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (username TEXT, question TEXT, answer TEXT, quiz TEXT)''')
    conn.commit()
    conn.close()

def save_progress(username, question, answer, quiz=""):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO progress VALUES (?, ?, ?, ?)", (username, question, answer, quiz))
    conn.commit()
    conn.close()

def get_progress(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM progress WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data

# --- Mentor AI Tutor function ---
def mentor_ai_tutor(question, premium=False, quiz=False):
    system_prompt = "You are Mentor AI Tutor, a super smart and patient AI tutor."
    if premium:
        system_prompt += " Provide detailed step-by-step explanations."
        if quiz:
            system_prompt += " Also provide a short 3-question quiz for the topic."
    else:
        system_prompt += " Provide a simple explanation suitable for students."

    # --- Use gpt-3.5-turbo to avoid 404 error ---
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Free-tier compatible
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
