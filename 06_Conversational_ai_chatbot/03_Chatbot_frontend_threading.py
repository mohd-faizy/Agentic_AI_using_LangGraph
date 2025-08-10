# ****************************************************************************************
# -> add a sidebar with title + A Start Chat Button + A title named 'Conversations History' 
# -> generate dynamic thread Id using UUID and add it to the session
# -> Display the thread id in sidebar

#----------------------------------------------------------------------------------------

# -> On Click of new chat open a new chat window
#    * Generate a new thread_id
#    * Save it in session
#    * Reset message history

#----------------------------------------------------------------------------------------

# -> create a list to store all thread_ids
# -> Load all the thread ids in the sidebar
# -> convert the side bar text to clickable buttons

#----------------------------------------------------------------------------------------

# -> on click of a particular thread id load that particular conversation

# ****************************************************************************************

# imports
import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot               # Import compiled LangGraph chatbot
import uuid


# **************************************************************************************************
# ----------------------------------------Utility Functions-----------------------------------------
# **************************************************************************************************
def generate_thread_id():
    '''Generate a unique thread ID for each conversation.'''
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    '''Reset the chat by clearing the message history and generating a new thread ID.'''
    st.session_state['thread_id'] = generate_thread_id()
    add_thread_id_to_history(st.session_state['thread_id'])  # also add new thread ID to history while resetting
    st.session_state['message_history'] = []                 # Initialize with empty chat history

def add_thread_id_to_history(thread_id):
    '''Add the current thread ID to the conversation history.'''
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    '''Load a specific conversation by thread ID.'''
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']

# **************************************************************************************************
# -------------------------------------------Session State------------------------------------------ 
# **************************************************************************************************
# st.session_state -> Dictionary to persist data across reruns (e.g., message history)
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []  # Initialize with empty chat history


# Generating the thread-id and adding it to the session state
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

# Chat Threads management 
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread_id_to_history(st.session_state['thread_id'])  # Add the current thread ID to the history




# **************************************************************************************************
# --------------------------------------------Sidebar UI-------------------------------------------- 
# **************************************************************************************************
st.sidebar.title("Langgraph Chatbot")

if st.sidebar.button("New Chat"): # On click of new chat
    reset_chat()                  # Reset chat history and generate new thread ID

st.sidebar.header("Conversation History")

# Display all thread IDs in the sidebar
for thread_id in st.session_state['chat_threads'][::-1]: 
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id  # Set the clicked thread ID
        messages = load_conversation(thread_id)    # Load messages for the selected thread

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages

# **************************************************************************************************
# ----------------------------------------------Main UI--------------------------------------------- 
# **************************************************************************************************

# loading the conversation history
# --------------------------------
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):     # Roles: 'user' or 'assistant'
        st.text(message['content'])            # Render message content in the UI

# [{'role': 'user', 'content': 'Hello!'}, {'role': 'assistant', 'content': 'Hi there! How can I help you today?'}]


# Chat Input Box
# --------------
user_input = st.chat_input('Type here...')

if user_input:
    # Append user's input to history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    # Display user's message in UI
    with st.chat_message('user'):
        st.text(user_input)
    
    # Configuration
    # -------------
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}} # Thread ID for LangGraph context  


    # LangGraph Streaming Section
    # ---------------------------
    with st.chat_message('assistant'):
        # Use Streamlit's write_stream to render assistant response token-by-token
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(   # Extract content from streamed message
                {'messages': [HumanMessage(content=user_input)]},                  # User input as initial state
                config=CONFIG,                                                     # Same thread ID to maintain context
                stream_mode='messages'                                             # Enable streaming response
            )
        )

    # Store assistant's full streamed message in chat history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
