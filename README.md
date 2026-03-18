<div align="center">
  <img src="_img/banner.png" alt="Agentic AI with LangGraph"/>

  <h1>Agentic AI with LangGraph</h1>
  
  <p>
    <b>Build autonomous, stateful, and goal-oriented AI systems capable of complex multi-step reasoning.</b>
  </p>

  <!-- Badges -->
  <p>
    <a href="https://github.com/mohd-faizy/Agentic_AI_using_LangGraph/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/LangGraph-Agentic%20Framework-blue?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph" />
    <img src="https://img.shields.io/badge/LangChain-Tooling-00ADD8?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain" />
    <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-0C0D0E?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  </p>

  <br />
</div>

---

## 📖 Overview

This repository demonstrates the comprehensive implementation of **Agentic AI** systems using **LangGraph**. Unlike traditional stateless Generative AI, this framework enables the creation of **autonomous agents** that can plan, execute, remember context, and collaborate to solve complex tasks.

It serves as both a **learning curriculum** and a **reference implementation** for building production-ready agentic workflows, covering everything from basic sequential chains to complex multi-agent orchestration with the **Model Context Protocol (MCP)**.

### 🧬 What is AgenticAI?

AgenticAI describes systems defined by:
*   **Autonomy**: Agents independently plan and execute subtasks.
*   **Orchestration**: Workflows are coordinated via a shared protocol (MCP).
*   **Composability**: Agents and graphs are modular, reusable, and testable.

---

## 🛣️ Roadmap & Curriculum

<div align="center">
  <img src="_img/agentic-AI-roadmap.png" alt="AgenticAI Roadmap"/>
</div>

### 🎓 Learning Path
*   **Foundation Level**
    *   ***Foundations of Agentic AI***: Core concepts and principles
    *   ***LangGraph Fundamentals***: State machines and workflow design
*   **Intermediate Level**
    *   ***Advanced LangGraph***: Complex routing and error handling
    *   ***AI Agents***: Agent design patterns and architectures
*   **Advanced Level**
    *   ***Agentic RAG***: Retrieval-augmented generation with agents
    *   ***Production Deployment***: Scaling and monitoring strategies

<div align="center">
  <img src="_img/map.png" alt="Curriculum Map"/>
</div>

---

## 🛠️ Core Components

The system is built around these modular and interoperable components:

1.  **Agents**
    *   *Description:* Autonomous entities with specific roles, memory, tools, and objectives.
    *   *Examples:* `PlannerAgent` (decomposes goals), `ResearchAgent` (gathers data), `ExecutionAgent` (runs tasks).

2.  **LangGraph State Machine**
    *   *Description:* The central orchestrator defining agent transitions, execution flow, and dynamic task routing.
    *   *Key Features:* Warning-Stateful DAG, Conditional Routing, Concurrency & Retries.

3.  **MCP Message Layer**
    *   *Description:* Protocol for structured message exchange including `Message`, `Thread`, `Step`, and `Run` objects to trace agent reasoning.

4.  **Memory and Context Store**
    *   *Description:* Long-term and short-term memory (Thread-level history, Agent-specific context, Vector DBs for RAG).

5.  **Tools and Interfaces**
    *   *Description:* External capabilities (Web search, Code interpreter, API clients) abstracted as callable nodes.

6.  **Task Router / Controller**
    *   *Description:* Mechanism for Centralized Planning or Distributed Negotiation to assign subtasks.

7.  **Observability & Debugging**
    *   *Description:* Logging, tracing, and monitoring via LangGraph visualizer and logging middleware.

---

## ⚖️ GenAI vs AgenticAI

| Feature | Generative AI (GenAI) | Agentic AI |
| :--- | :--- | :--- |
| **Primary Output** | Unstructured content (text, image, audio) | Structured outputs from autonomous task execution |
| **Execution Flow** | Stateless, single-step inference | Stateful, iterative multi-step reasoning with memory |
| **Architecture** | Monolithic linear pipelines | Modular, event-driven multi-agent systems (DAGs) |
| **Decision-Making** | Prompt-conditioned output | Goal-oriented planning & dynamic context tracking |
| **Autonomy** | Passive response to queries | Proactive decision-making |
| **Control Flow** | Prompt engineering | Finite-state machines & reactive policies |
| **Memory** | Ephemeral (limited context) | Persistent, structured memory |
| **Tool Use** | Manually scripted / templates | Dynamic tool selection via MCP |
| **Scalability** | Limited by model/context size | Horizontal scaling via specialized agents |
| **Debuggability** | Opaque reasoning | Transparent workflows & traceable nodes |

---

## 📂 Notebook Index

| S.No | Notebook Name | Topic Covered | Link |
| :---: | :--- | :--- | :--- |
| **01** | `01_RoadMap.ipynb` | Comprehensive roadmap for learning Agentic AI with LangGraph | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](01_Foundation_of_AgenticAI/01_RoadMap.ipynb) |
| **02** | `02_GenAI_vs_AgenticAI.ipynb` | Differences between Generative AI and Agentic AI | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](01_Foundation_of_AgenticAI/02_GenAI_vs_AgenticAI.ipynb) |
| **03** | `03_AgenticAI_Core_Concepts.ipynb` | Core concepts and principles of Agentic AI | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](01_Foundation_of_AgenticAI/03_AgenticAI_Core_Concepts.ipynb) |
| **04** | `04_LangChain_vs_langGraph.ipynb` | Comparison between LangChain and LangGraph | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](01_Foundation_of_AgenticAI/04_LangChain_vs_langGraph.ipynb) |
| **05** | `05_LangGraph_Core_Concepts.ipynb` | Core concepts and architecture of LangGraph | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](01_Foundation_of_AgenticAI/05_LangGraph_Core_Concepts.ipynb) |
| **06** | `06_Sequential_Workflows.ipynb` | Building linear and sequential chain executions | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](02_%20Sequential_&_Parallel_workflow/06_Sequential_Workflows.ipynb) |
| **07** | `07_Parallel_workflow.ipynb` | Implementing parallel workflow executions | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](02_%20Sequential_&_Parallel_workflow/07_Parallel_workflow.ipynb) |
| **08** | `08_Conditional_Workflow.ipynb` | Dynamic routing based on logic (Router) | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](03_Conditional_Workflow/08_Conditional_Workflow.ipynb) |
| **09** | `09_Iterative_workflows.ipynb` | Creating loops and retry mechanisms in workflows | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](04_Iterative_Workflows/09_Iterative_workflows.ipynb) |
| **10** | `10_Chatbot.ipynb` | Building a structured AI chatbot | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](05_Structured_ai_chatbot/10_Chatbot.ipynb) |
| **11** | `11_Persistence_LangGraph.ipynb` | Implementing memory and persistence in LangGraph workflows | [![Open Notebook](https://img.shields.io/badge/Open_Notebook-1572B6?style=flat&logo=Jupyter&logoColor=white)](05_Structured_ai_chatbot/11_Persistence_LangGraph.ipynb) |
| **12** | `12_LangsSmith.ipynb` | LangSmith integration and tracing | ⏳ *Pending Upload* |
| **13** | `13_Observability_in_LangGraph.ipynb` | Observability and monitoring in LangGraph | ⏳ *Pending Upload* |
| **14** | `14_Tools_in_LangGraph.ipynb` | Using tools with LangGraph agents | ⏳ *Pending Upload* |
| **15** | `15_MCP_Client.ipynb` | Model Context Protocol implementation | ⏳ *Pending Upload* |
| **16** | `16_RAG_using_LangGraph.ipynb` | Retrieval-Augmented Generation workflows | ⏳ *Pending Upload* |
| **17** | `17_Human_in_the_Loop.ipynb` | Human-in-the-loop approvals and modifications | ⏳ *Pending Upload* |
| **18** | `18_Subgraphs.ipynb` | Building and orchestrating subgraphs | ⏳ *Pending Upload* |
| **19** | `19_Memory_in_LangGraph.ipynb` | Advanced memory management with LangGraph | ⏳ *Pending Upload* |
| **20** | `20_Projects.ipynb` | End-to-end Agentic AI projects | ⏳ *Pending Upload* |

---

## 🚀 Getting Started

### Prerequisites
*   **Python 3.9+**
*   **Git**
*   **API Keys**: OpenAI, Anthropic, or HuggingFace.

### Installation

We recommend using `uv` for fast dependency management, but standard `pip` works as well.

1.  **Clone the repository**
    ```bash
    git clone https://github.com/mohd-faizy/Agentic_AI_using_LangGraph.git
    cd Agentic_AI_using_LangGraph
    ```

2.  **Set up the environment**

    *Using `uv` (Recommended):*
    ```bash
    uv venv
    source .venv/bin/activate       # macOS/Linux
    .venv\Scripts\activate          # Windows
    uv add -r requirements.txt
    ```

    *Using `pip`:*
    ```bash
    python -m venv venv
    source venv/bin/activate        # macOS/Linux
    venv\Scripts\activate           # Windows
    pip install -r requirements.txt
    ```

3.  **Configuration**
    Create a `.env` file:
    ```bash
    cp .env.example .env
    ```
    Add your keys:
    ```ini
    OPENAI_API_KEY=sk-...
    LANGCHAIN_API_KEY=...
    ```

## ⚡ Quick Start

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

# 1. Define State
class AgentState(TypedDict):
    messages: list

# 2. Define Nodes
def agent_node(state: AgentState):
    return {"messages": ["Agent processing..."]}

# 3. Build Graph
workflow = StateGraph(AgentState)
workflow.add_node("agent", agent_node)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)

# 4. Compile & Run
app = workflow.compile()
print(app.invoke({"messages": ["Init"]}))
```

---

## 🤝 Contributing & Support

Contributions are welcome! If you find this repository helpful, please **star** it!

<div align="center">
  <br>
  <p><b>Connect with me</b></p>
  <a href="https://twitter.com/F4izy"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mohd-faizy/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/mohd-faizy"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a>
</div>

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
