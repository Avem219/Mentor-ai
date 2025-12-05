import streamlit as st
from utils import get_progress

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
st.title("📊 Progress Dashboard")

username = st.text_input("Enter your username to see progress:")

if username:
    data = get_progress(username)
    if data:
        st.write(f"Total Questions Asked: {len(data)}")
        premium_quizzes = len([d for d in data if d[3] == "Yes"])
        st.write(f"Premium Quizzes Generated: {premium_quizzes}")
        for d in data:
            st.markdown(f"**Q:** {d[1]}  \n**A:** {d[2]}  \n**Quiz:** {d[3]}")
    else:
        st.write("No progress found.")
