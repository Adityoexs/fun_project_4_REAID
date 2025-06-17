# AIO Chatbot Powered by OpenRouter

This AIO Chatbot is powered by **OpenRouter** and **OpenAI's GPT-3.5-turbo** model. It allows users to interact with an AI assistant, ask questions, and receive intelligent responses. The chatbot is implemented using **Streamlit** for an interactive web-based interface.

## Features

- **AIO Chat Interaction**: The chatbot processes user input and returns a response based on OpenAI's GPT-3.5-turbo model.
- **History**: All previous chat interactions are displayed in a scrollable chat history.
- **Feedback**: Users can provide feedback on the assistant's response.
- **Validation**: Ensures the user provides valid input and handles API errors gracefully.

## Preview

![Screenshot 2025-06-17 174513](https://github.com/user-attachments/assets/78492431-668d-4ffa-aee8-ba5989165fd0)
![Screenshot 2025-06-17 174517](https://github.com/user-attachments/assets/bff5639c-1bc1-47fb-aa79-877688a8405b)
![Screenshot 2025-06-17 174523](https://github.com/user-attachments/assets/c46c20fe-36f1-4f38-b422-6f34d44074de)
*AIO Chatbot Interface Preview*  
  
Here’s what the interface looks like:

- **Chat History**: Shows past interactions with the chatbot, categorized into "You" (user input) and "Assistant" (bot responses).
- **User Input Box**: Users can type their messages and receive responses in real-time.
- **Feedback**: After the assistant responds, users can leave feedback for improvement.

## How to Run

### Prerequisites

1. Install **Streamlit** and **Requests** libraries in your Python environment.
   
   ```bash
   pip install streamlit requests
