import streamlit as st
import requests
from dotenv import load_dotenv
import os


# CONFIG API KEY
load_dotenv() 

OPENROUTER_API_KEY = os.getenv("API_KEY")
MODEL = "openai/gpt-3.5-turbo"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://openrouter.ai",
    "Content-Type": "application/json",
    "X-title": "AI Chatbot",
}

API_URL = f"https://openrouter.ai/api/v1/chat/completions"

#===================================
# Streamlit UI Configuration
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Header and Introduction
st.title("AIO Chatbot")
st.markdown(f"Powered by [Open AI](https://openrouter.ai) and 'OpenRouter'. 🤖")
st.markdown("""
    **Chat with the AI assistant** below.  
    Type your message and get a response from the bot. Feel free to ask anything!
""")

# Sidebar for app information and settings
with st.sidebar:
    st.header("About the AI Chatbot")
    st.write("""
        This AI chatbot is powered by OpenRouter using OpenAI's GPT-3.5-turbo model.  
        You can ask it anything, and it will provide helpful responses based on your queries.
    """)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history in a nice layout
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        if chat["role"] == "user":
            st.markdown(f"**You**: {chat['content']}")
        else:
            st.markdown(f"**Assistant**: {chat['content']}")

# User Input Area with validation
user_input = st.chat_input("Type your message here...")

if user_input:
    if len(user_input.strip()) == 0:
        st.warning("Please enter a valid message.")
    else:
        st.chat_message("user").markdown(f"**You**: {user_input}")
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("AI is thinking... 🧠💬"):
            # Preparing payload for API request
            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "user", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            }

            # Make the API call to get the AI response
            try:
                response = requests.post(API_URL, headers=HEADERS, json=payload)
                response.raise_for_status()  # Raise an exception for bad status codes
                bot_reply = response.json()["choices"][0]["message"]["content"]
            except requests.exceptions.RequestException as e:
                bot_reply = f"Error fetching response from the API: {e}"

        if response.status_code == 401:
            bot_reply = "Unauthorized: API key mungkin salah atau tidak valid. Silakan periksa API key Anda. {response.status_code} - {response.text}"
        elif response.status_code == 200:
            bot_reply = response.json()["choices"][0]["message"]["content"]
        else:
            bot_reply = "Gagal mendapatkan jawaban dari AI. Periksa koneksi atau coba lagi nanti. {response.status_code} - {response.text}"


        # Display assistant's message in a nice format
        st.chat_message("assistant").markdown(f"**Assistant**: {bot_reply}")
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

        # Add a feedback button for users
        feedback = st.text_area("Let us know your thoughts about this reply:", key="feedback_area")
        
        if st.button("Provide Feedback", key="feedback_button"):
            if len(feedback.strip()) == 0:
                st.warning("Please provide some feedback before submitting.")
            else:
                st.success("Thank you for your feedback!")
                # You can handle the feedback storage or sending it to an API if needed

else:
    st.info("Type your message in the input box above to start chatting.")
