# AIO Chatbot Powered by OpenRouter

This AIO Chatbot is powered by **OpenRouter** and **OpenAI's GPT-3.5-turbo** model. It allows users to interact with an AI assistant, ask questions, and receive intelligent responses. The chatbot is implemented using **Streamlit** for an interactive web-based interface.

## Features

- **AIO Chat Interaction**: The chatbot processes user input and returns a response based on OpenAI's GPT-3.5-turbo model.
- **History**: All previous chat interactions are displayed in a scrollable chat history.
- **Feedback**: Users can provide feedback on the assistant's response.
- **Validation**: Ensures the user provides valid input and handles API errors gracefully.

## Preview

![Screenshot 2025-06-17 175649](https://github.com/user-attachments/assets/a3d73365-187b-4c97-8fea-a41a5ea4f578)
![Screenshot 2025-06-17 175654](https://github.com/user-attachments/assets/7f13db40-2982-45d0-9986-2f2ed826041b)
![Screenshot 2025-06-17 175729](https://github.com/user-attachments/assets/38e7e8b6-55d3-4bb5-aafc-c27c069f439f)

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
