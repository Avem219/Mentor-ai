import streamlit as st
from utils import mentor_ai_tutor, save_progress, init_db

# --- Futuristic theme styling ---
st.set_page_config(page_title="Mentor AI Tutor", page_icon="🤖", layout="wide")
st.markdown("""
    <style>
    body { background-color: #0f111a; color: #00fff7; }
    .stTextInput>div>div>input { background-color: #1b1f36; color: #00fff7; border: 1px solid #00fff7; }
    .stButton>button { background-color: #00fff7; color: #0f111a; font-weight: bold; }
    .stMarkdown { font-family: 'Orbitron', sans-serif; }
    </style>
""", unsafe_allow_html=True)

# Initialize database
init_db()

def main():
    st.title("🤖 Mentor AI Tutor - Home")
    username = st.text_input("Enter your username")
    premium_user = st.checkbox("Premium User (Step-by-step + Speechify + Quiz)")

    question = st.text_input("Ask your question")
    quiz_mode = False
    if premium_user:
        quiz_mode = st.checkbox("Generate Quiz for this question")

    if st.button("Ask Mentor AI Tutor") and question and username:
        with st.spinner("Thinking..."):
            answer = mentor_ai_tutor(question, premium=premium_user, quiz=quiz_mode)
            st.markdown(f"**Mentor AI Tutor says:**\n\n{answer}")
            save_progress(username, question, answer, quiz="Yes" if quiz_mode else "No")

            # Speechify for Premium users
            if premium_user:
                st.markdown(f"""
                <script>
                var msg = new SpeechSynthesisUtterance();
                msg.text = `{answer.replace("\\n", " ")}`;
                window.speechSynthesis.speak(msg);
                </script>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
