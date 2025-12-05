import streamlit as st
from utils import get_progress

st.set_page_config(page_title="Quizzes", page_icon="📝", layout="wide")
st.title("📝 Quizzes Page")

username = st.text_input("Enter your username to see quizzes:")

if username:
    data = get_progress(username)
    quizzes = [d for d in data if d[3] == "Yes"]
    if quizzes:
        for i, q in enumerate(quizzes, 1):
            st.subheader(f"Quiz {i} - Question: {q[1]}")
            st.write(q[2])
    else:
        st.write("No quizzes found. Premium users can generate quizzes from Home page.")
