import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot  # Import compiled LangGraph chatbot

# Configuration
# -------------------------------
CONFIG = {'configurable': {'thread_id': 'thread-1'}}  # Optional thread ID for LangGraph context

# Session State Initialization
# -------------------------------
# st.session_state -> Dictionary to persist data across reruns (e.g., message history)
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []  # Initialize with empty chat history


# Display Previous Chat Messages
# -------------------------------
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):     # Roles: 'user' or 'assistant'
        st.text(message['content'])            # Render message content in the UI


# Chat Input Box
# -------------------------------
user_input = st.chat_input('Type here...')

if user_input:
    # Append user's input to history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    # Display user's message in UI
    with st.chat_message('user'):
        st.text(user_input)


    # LangGraph Streaming Section
    # -------------------------------
    with st.chat_message('assistant'):
        # Use Streamlit's write_stream to render assistant response token-by-token
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(   # Extract content from streamed message
                {'messages': [HumanMessage(content=user_input)]},                  # User input as initial state
                config={'configurable': {'thread_id': 'thread-1'}},                # Same thread ID to maintain context
                stream_mode='messages'                                             # Enable streaming response
            )
        )

    # Store assistant's full streamed message in chat history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
