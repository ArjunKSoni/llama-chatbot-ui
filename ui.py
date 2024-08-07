import streamlit as st
import requests

CHAT_URL = "https://llamachat-ipea.onrender.com/chat"
ASK_URL = "https://llamachat-ipea.onrender.com/ask"
SEARCH_URL = "https://llm-search-agent-api.onrender.com/search"

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

def stream(response, response_text):
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            data=chunk.decode('utf-8')
            response_text += data
            yield data
    st.session_state.chat_history.append({"role": "bot", "content": response_text})


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
    
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.chat_message(USER).write(message['content'])
        else:
            st.chat_message(BOT).write(message['content'])
    
    response_text = ""
    st.chat_message(BOT).write(stream(response, response_text))
    
