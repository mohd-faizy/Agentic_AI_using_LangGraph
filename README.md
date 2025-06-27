# 🤖 AgenticAI using LangGraph & MCP

> A modular, scalable reference implementation for building **Agentic Multi-Agent Systems** leveraging LangGraph and the **Model Context Protocol (MCP)**—designed to orchestrate autonomous, goal-driven agents with composable execution graphs, asynchronous interactions, and context-aware decision making.

<div align="center">
  <img src="YOUR_IMAGE_URL_HERE" alt="Agentic AI Overview" width="800"/>
  <p><em>High-level architecture of AgenticAI workflows</em></p>
</div>

---

![author](https://img.shields.io/badge/author-mohd--faizy-red)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Framework-blue?logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-MCP-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Model%20Serving-0C0D0E?logo=ollama&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLMs-yellow?logo=huggingface&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-Tooling-00ADD8?logo=langchain&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📚 Table of Contents

- [🤖 AgenticAI using LangGraph \& MCP](#-agenticai-using-langgraph--mcp)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [🧬 What is AgenticAI?](#-what-is-agenticai)
  - [🛠️ Core Components](#️-core-components)
  - [🧠 GenAI vs AgenticAI](#-genai-vs-agenticai)
  - [⚙️ Installation](#️-installation)
  - [Contributing](#contributing)
  - [⚖ ➤ License](#--license)
  - [❤️ Support](#️-support)
  - [🪙Credits and Inspiration](#credits-and-inspiration)
  - [🔗Connect with me](#connect-with-me)

---

## 🔍 Overview

This reference implementation demonstrates how to:

- Combine **LangGraph** for compositional agent graphs  
- Leverage **Model Context Protocol (MCP)** for standardized tool/context integration  
- Employ **Ollama** & **HuggingFace** models for domain‐specific intelligence  

…to build **production-grade, goal-driven** AI systems with:

- Fine-grained task decomposition  
- Context-aware reasoning  
- Event-driven, asynchronous coordination  
- Human-in-the-loop feedback loops  

---

## 🧬 What is AgenticAI?

AgenticAI describes systems where:

- **Autonomy**: Agents independently plan and execute subtasks  
- **Orchestration**: Workflows are coordinated via a shared protocol (MCP)  
- **Composability**: Agents and graphs are modular, reusable, and testable  

These systems extend beyond classic Generative AI by providing **stateful**, **goal-oriented** workflows across multiple collaborative agents.

---

## 🛠️ Core Components

- **LangGraph**  
  Build and visualize multi-agent workflows as directed graphs.  

- **MCP (Model Context Protocol)**  
  A JSON-RPC–style standard for exposing tools, data sources, and context to LLM-powered agents.  

- **Ollama**  
  High-throughput LLM serving for on-premise or cloud deployments.  

- **HuggingFace Models**  
  Domain-tuned transformers for specialized reasoning tasks.  

---

## 🧠 GenAI vs AgenticAI

| Feature                    | Generative AI (GenAI)                                                    | Agentic AI                                                                 |
|----------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Primary Output**         | Unstructured content (text, image, audio, video)                         | Structured outputs from autonomous task execution                         |
| **Execution Flow**         | Stateless, single-step inference per prompt                             | Stateful, iterative multi-step reasoning with memory                      |
| **Architecture**           | Monolithic or linear prompt pipelines                                    | Modular, event-driven multi-agent systems (e.g., DAGs in LangGraph)       |
| **Decision-Making Paradigm**| Prompt-conditioned output generation                                     | Goal-oriented planning with long-term memory and dynamic context tracking |
| **Autonomy**               | Passive response to human queries                                       | Proactive decision-making and self-directed task execution                |
| **Control Flow Logic**     | Determined by prompt engineering                                        | Driven by finite-state machines, graphs, or reactive policies             |
| **Memory & State Handling**| Typically ephemeral (no memory or limited through hacks like RAG)       | Persistent, structured memory for state tracking and dependency handling  |
| **Interactivity Level**    | Low—requires repeated user input                                        | High—agents plan, recover from failure, and reattempt subtasks            |
| **Tool Use & API Calling** | Manually scripted via code or prompt templates                          | Dynamically selected tools via agent/tool registries and MCP mechanisms   |
| **Adaptability**           | Fixed behavior per prompt configuration                                 | Context-aware adaptation based on task state and environment              |
| **Scalability**            | Scaling limited by model size and prompt length                         | Scales horizontally by orchestrating multiple specialized agents          |
| **Debuggability**          | Opaque reasoning; difficult to trace                                    | Transparent workflows; traceable node-level decisions                     |
| **Learning/Training**      | Pretrained foundation models; static behavior                           | Potential for online learning, fine-tuning per agent                      |
| **Security/Guardrails**    | Prompt filtering, static constraints                                    | Embedded policies, role-based access, task-level validation               |
| **Deployment Targets**     | Front-end apps, content generators, creative tools                      | Backend automation, orchestration layers, autonomous agent systems        |
| **Example Systems**        | ChatGPT, Claude, Gemini, DALL·E 3, Sora, MusicLM, MidJourney             | AutoGPT, LangGraph + MCP, OpenDevin, OpenAgents, CrewAI, MetaAgent, Devika |


---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/mohd-faizy/Agentic_AI_using_LangGraph_-_MCP.git
cd Agentic_AI_using_LangGraph_-_MCP

# 2. Create & activate a virtual environment
python -m venv venv
# Unix/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

```


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚖ ➤ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

## ❤️ Support

If you find this repository helpful, show your support by starring it! For questions or feedback, reach out on [Twitter(`X`)](https://twitter.com/F4izy).

## 🪙Credits and Inspiration

This repository draws inspiration from the exceptional educational content developed by Nitish, Krish Naik, and the DataCamp course `Developing LLMs with LangChain`. The implementations and examples provided here are grounded in their comprehensive tutorials on Generative AI, with a particular focus on LangChain and Hugging Face.

## 🔗Connect with me

➤ If you have questions or feedback, feel free to reach out!!!

[<img align="left" src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/twitter_circle-512.png" width="32px"/>][twitter]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="32px"/>][linkedin]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/2626/2626299.png" width="32px"/>][Portfolio]

[twitter]: https://twitter.com/F4izy
[linkedin]: https://www.linkedin.com/in/mohd-faizy/
[Portfolio]: https://ai.stackexchange.com/users/36737/faizy?tab=profile

---

<img src="https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true" width=380px height=200px />
