import streamlit as st
import sqlite3

st.set_page_config(page_title="Profile", page_icon="⚙️", layout="wide")
st.title("⚙️ Profile / Settings")

username = st.text_input("Enter your username:")

if username:
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (username, premium) VALUES (?, ?)", (username, 0))
    conn.commit()
    
    premium = st.radio("Premium Status:", ("Free", "Premium"))
    premium_val = 1 if premium=="Premium" else 0
    c.execute("UPDATE users SET premium=? WHERE username=?", (premium_val, username))
    conn.commit()
    conn.close()
    
    st.success(f"User {username} updated to {premium}!")
