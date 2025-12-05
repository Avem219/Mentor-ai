import openai
import sqlite3
import os

# Get API key from environment variable (Streamlit Secrets)
OPENAI_API_KEY = os.getenv("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")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, premium INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (username TEXT, question TEXT, answer TEXT, quiz TEXT)''')
    conn.commit()
    conn.close()

# Save user progress
def save_progress(username, question, answer, quiz=""):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO progress VALUES (?, ?, ?, ?)", (username, question, answer, quiz))
    conn.commit()
    conn.close()

# Get user progress
def get_progress(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM progress WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data

# Mentor AI Tutor function using new OpenAI API
def mentor_ai_tutor(question, premium=False, quiz=False):
    system_prompt = "You are Mentor AI Tutor, a super smart and patient AI tutor."
    if premium:
        system_prompt += " Provide detailed step-by-step explanations."
        if quiz:
            system_prompt += " Also provide a short 3-question quiz for the topic."
    else:
        system_prompt += " Provide a simple explanation suitable for students."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
