import streamlit as st
from main import chat

st.set_page_config(page_title="JarvisAI", page_icon="🤖")
st.title("JarvisAI - Interactive Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = ""

user_input = st.text_input("Ask Jarvis something:")

if st.button("Send"):
    if user_input.strip():
        st.session_state['chat_history'] += f"You: {user_input}\n"
        response = chat(user_input, st.session_state['chat_history'])
        st.session_state['chat_history'] += f"Jarvis: {response}\n"
        st.experimental_rerun()

st.text_area("Conversation", st.session_state['chat_history'], height=400, key="history", disabled=True) 