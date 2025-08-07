# Import required classes and functions for LangGraph
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize language model 
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define a shared state structure for the LangGraph pipeline
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]  # messages will be persisted and passed between nodes

# Define a LangGraph node function to process chat messages
def chat_node(state: ChatState):
    messages = state["messages"]     # Extract previous messages from state
    response = llm.invoke(messages)  # Generate response using the LLM
    return {"messages": [response]}  # Return the new message to update the state

# Initialize an in-memory checkpointer to store intermediate state
checkpointer = InMemorySaver()

# Create the LangGraph stateful graph
graph = StateGraph(ChatState)  # Pass the expected state type here

# Add a node 
graph.add_node("chat_node", chat_node)

# Define the edges
graph.add_edge(START, "chat_node")  # Execution starts at "chat_node"
graph.add_edge("chat_node", END)    # After processing, the flow ends

# Compile the graph into an executable chatbot with checkpointing
chatbot = graph.compile(checkpointer=checkpointer)



