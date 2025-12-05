import streamlit as st
from utils import mentor_ai_tutor, save_progress, init_db

def main():
    # Initialize database
    init_db()

    # App title
    st.title("🧠 Mentor AI Tutor - Home")

    # User input
    username = st.text_input("Enter your username:")
    premium_user = st.checkbox("Premium User (Step-by-step + Speechify + Quiz)")

    user_question = st.text_input("Ask your question:")

    # Quiz option for Premium users
    quiz_mode = False
    if premium_user:
        quiz_mode = st.checkbox("Generate Quiz for this question")

    # Process question when button is clicked
    if st.button("Ask Mentor AI Tutor") and user_question and username:
        with st.spinner("Thinking..."):
            answer = mentor_ai_tutor(user_question, premium=premium_user, quiz=quiz_mode)
            st.markdown(f"**Mentor AI Tutor says:**\n\n{answer}")

            # Save progress
            save_progress(username, user_question, answer, quiz="Yes" if quiz_mode else "No")

            # Speechify for Premium users
            if premium_user:
                st.markdown(f"""
                <script>
                var msg = new SpeechSynthesisUtterance();
                msg.text = `{answer.replace("\\n", " ")}`;
                window.speechSynthesis.speak(msg);
                </script>
                """, unsafe_allow_html=True)

# --- Main entry point ---
if __name__ == "__main__":
    main()