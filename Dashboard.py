import streamlit as st
from utils import get_progress

st.title("📊 Progress Dashboard")
username = st.text_input("Enter your username:")

if username:
    data = get_progress(username)
    if data:
        st.write(f"Total Questions Asked: {len(data)}")
        premium_questions = len([d for d in data if d[3] == "Yes"])
        st.write(f"Premium Quizzes Generated: {premium_questions}")
        for d in data:
            st.markdown(f"**Q:** {d[1]}  \n**A:** {d[2]}  \n**Quiz:** {d[3]}")
    else:
        st.write("No progress found.")