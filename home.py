import streamlit as st
from utils import mentor_ai_tutor

st.set_page_config(
    page_title="Mentor AI Tutor",
    page_icon="📘",
    layout="wide"
)

st.markdown("""
<div style='text-align:center;'>
  <h1 style="font-size:40px; color:#10a37f;">Mentor AI Tutor 🤖📘</h1>
  <p style="color:#555;">Ask anything & get smart, simple explanations.</p>
</div>
""", unsafe_allow_html=True)

username = st.text_input("Enter your name:")

premium_user = st.toggle("🌟 Premium Mode (step-by-step + quizzes + voice)")

question = st.text_area("Your Question", height=150)

if st.button("Ask Mentor AI"):
    with st.spinner("Thinking…"):
        reply = mentor_ai_tutor(question, premium=premium_user)
        st.markdown(f"""
        <div style='background:#f7f7f8; padding:20px; border-radius:12px;'>
            {reply}
        </div>
        """, unsafe_allow_html=True)
