# app.py

import streamlit as st
import openai
import os

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Java's Coffee Chat ☕️", page_icon="☕️", layout="centered")

# Make sure your OpenAI API key is set in environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# SESSION STATE
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "refresh" not in st.session_state:
    st.session_state.refresh = False

# -----------------------------
# FUNCTIONS
# -----------------------------
def send_prompt(prompt):
    """Send user prompt to OpenAI API and get a response."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or gpt-3.5-turbo if using ChatCompletion
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# -----------------------------
# UI
# -----------------------------
st.title("☕ Java's Coffee Chat")
st.write("Pull up a chair, drop a prompt, and let the barista (LLM) pour answers!")

# Input
user_input = st.text_input("Your Question:", "")

if st.button("Send"):
    if user_input.strip() != "":
        answer = send_prompt(user_input)
        st.session_state.chat_history.append({"user": user_input, "bot": answer})
        # Safe rerun
        st.session_state.refresh = not st.session_state.refresh
        st.experimental_rerun()

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Barista:** {chat['bot']}")
    st.markdown("---")

# Optional: clear chat
if st.button("☕ Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
