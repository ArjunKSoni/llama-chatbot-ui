import streamlit as st
import requests

CHAT_URL = "http://127.0.0.1:4000/chat"
ASK_URL = "http://127.0.0.1:4000/ask"
SEARCH_URL = "http://127.0.0.1:8000/search"

USER='User'
BOT='Assistant'


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


def call_chat_api(user_input):
    response = requests.post(CHAT_URL, json={"input": user_input}, stream=True)
    return response


def call_ask_api(user_input):
    response = requests.post(ASK_URL, json={"input": user_input}, stream=True)
    return response

def call_search_api(user_input):
    response = requests.post(SEARCH_URL, json={"input": user_input}, stream=True)
    return response

st.set_page_config(page_title="Chatbot")


st.sidebar.title("Select API")
api_choice = st.sidebar.radio("", ("Chat API", "Ask API", "Search API"))


st.title("Chatbot: Arjun Creation")


user_input = st.chat_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    if api_choice == "Chat API":
        response = call_chat_api(user_input)
    elif api_choice == "Ask API":
        response = call_ask_api(user_input)
    else:
        response = call_search_api(user_input)
    
    response_text = ""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            response_text += chunk.decode('utf-8')
    st.session_state.chat_history.append({"role": "bot", "content": response_text})
    
    
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.chat_message(USER).write(message['content'])
        else:
            st.chat_message(BOT).write(message['content'])
