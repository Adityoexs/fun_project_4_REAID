# AIO Chatbot Powered by OpenRouter

This AIO Chatbot is powered by **OpenRouter** and **OpenAI's GPT-3.5-turbo** model. It allows users to interact with an AI assistant, ask questions, and receive intelligent responses. The chatbot is implemented using **Streamlit** for an interactive web-based interface.

## Features

- **AIO Chat Interaction**: The chatbot processes user input and returns a response based on OpenAI's GPT-3.5-turbo model.
- **History**: All previous chat interactions are displayed in a scrollable chat history.
- **Feedback**: Users can provide feedback on the assistant's response.
- **Validation**: Ensures the user provides valid input and handles API errors gracefully.

## Preview

![Screenshot 2025-06-17 175649](https://github.com/user-attachments/assets/19fa526f-70cd-498b-914a-dbb899bf4548)
![Screenshot 2025-06-17 175654](https://github.com/user-attachments/assets/588d2221-ff80-491d-9fc7-401a539a8a19)
![Screenshot 2025-06-17 175729](https://github.com/user-attachments/assets/646cfd99-7e93-49a4-a999-ea50c8f5d91c)
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
