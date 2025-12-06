import os
from openai import OpenAI
import sqlite3

# Configure OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI-compatible client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

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
    c.execute("INSERT INTO progress VALUES (?, ?, ?, ?)",
              (username, question, answer, quiz))
    conn.commit()
    conn.close()

def get_progress(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM progress WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data

def mentor_ai_tutor(question, premium=False, quiz=False):
    system_prompt = "You are Mentor AI Tutor, a helpful and patient tutor for students."
    if premium:
        system_prompt += " Provide detailed step-by-step explanations."
        if quiz:
            system_prompt += " Also provide a short quiz at the end of your answer."
    else:
        system_prompt += " Provide a clear, simple explanation suitable for students."

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=512
    )

    return response.choices[0].message.content
