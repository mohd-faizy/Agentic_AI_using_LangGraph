from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
# from langgraph.checkpoint.memory import InMemorySaver [X]
from langgraph.checkpoint.sqlite import SqliteSaver 
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3


load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]  


def chat_node(state: ChatState):
    messages = state["messages"]     
    response = llm.invoke(messages)  
    return {"messages": [response]}  

# checkpointer = InMemorySaver() [X]

# Initialize SQLite connection
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)


graph = StateGraph(ChatState)  
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node") 
graph.add_edge("chat_node", END)   

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    """Retrieve all unique thread IDs from the database."""
    all_threads = set()                                                  # Initialize a set to store unique thread IDs
    for checkpoint in checkpointer.list(None):                           # List all checkpoints
        all_threads.add(checkpoint.config['configurable']['thread_id'])  # Add thread ID to the set
    return list(all_threads)                                             # Return the list of all unique thread IDs

