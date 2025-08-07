import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot # from chatbot_frontend.py

# configuration passed to the chatbot
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# st.session_state -> dictionary to store the conversation history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = [] # Store chat history as a list of message dictionaries

# Display previous messages from the session history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):   # 'role' should be either 'user' or 'assistant'
        st.text(message['content'])          # Show the message content in the chat window


# Chat input box for user to type a message
user_input = st.chat_input('Type here...')

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})       # Append the user's message to session history
    # Display the user's message in the chat interface
    with st.chat_message('user'):
        st.text(user_input)

    # Call the chatbot backend with the latest user message
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG) 
    ai_message = response['messages'][-1].content                                             # Extract the assistant's reply from the response
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})  # Append the assistant's response to session history
    # Display the assistant's reply in the chat interface
    with st.chat_message('assistant'):
        st.text(ai_message)