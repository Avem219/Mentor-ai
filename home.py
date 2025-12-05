import streamlit as st
from utils import mentor_ai_tutor, save_progress, init_db
import os

# --- Page config ---
st.set_page_config(page_title="Mentor AI Tutor", page_icon="🤖", layout="wide")

# --- Futuristic Theme CSS ---
st.markdown("""
<style>
body {
    background-color: #0f111a;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button {
    background-color: #00fff7;
    color: #0f111a;
    font-weight: bold;
    border-radius: 5px;
}
.chat-container {
    background-color: #1b1f36;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user-msg {
    background-color: #272b45;
    color: #00fff7;
    padding: 8px;
    border-radius: 10px;
    text-align: right;
}
.ai-msg {
    background-color: #00fff7;
    color: #0f111a;
    padding: 8px;
    border-radius: 10px;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# --- Initialize DB ---
init_db()

# --- Session state to store chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Sidebar for username and premium toggle ---
with st.sidebar:
    st.title("⚙️ Settings")
    username = st.text_input("Enter your username")
    premium_user = st.checkbox("Premium User (Step-by-step + Speechify + Quiz)")

# --- Chat interface ---
st.title("🤖 Mentor AI Tutor Chat")

user_input = st.text_input("Type your question here...")

# --- Button to send message ---
if st.button("Send") and user_input and username:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate AI response
    with st.spinner("Mentor AI Tutor is typing..."):
        try:
            answer = mentor_ai_tutor(user_input, premium=premium_user, quiz=False)
        except Exception as e:
            # Handle quota or other OpenAI errors gracefully
            answer = f"[Error fetching response] {str(e)}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        save_progress(username, user_input, answer, quiz="No")

        # Speechify for premium users
        if premium_user:
            st.markdown(f"""
            <script>
            var msg = new SpeechSynthesisUtterance();
            msg.text = `{answer.replace("\\n"," ")}`;
            window.speechSynthesis.speak(msg);
            </script>
            """, unsafe_allow_html=True)

# --- Display chat messages ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-container user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-container ai-msg">{msg["content"]}</div>', unsafe_allow_html=True)
