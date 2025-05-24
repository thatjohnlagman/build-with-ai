from google import genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# replace this later to use the env variable!!
client = genai.Client(api_key="os.getenv('GEMINI_API_KEY')")



st.title("Gemini Chatbot hehe")


# Session state
if "history" not in st.session_state:
    st.session_state.history = []

messages = st.container(height=850)

# Display previous chat history
for message in st.session_state.history:
    messages.chat_message(message["role"]).write(message["content"])


if prompt := st.chat_input("Say something", accept_file=True, file_type=["pdf"]):
    # Save user message
    st.session_state.history.append({"role": "user", "content": prompt["text"]})
    messages.chat_message("user").write(prompt["file"])
    
    # Generate and save assistant reply
    reply = f"Echo: {prompt["text"]}"
    st.session_state.history.append({"role": "assistant", "content": reply})
    messages.chat_message("assistant").write(reply)