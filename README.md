# ⚖️ Legal Document RAG Assistant (LangGraph + HITL)

##  Overview

This project is a **Retrieval-Augmented Generation (RAG)** system designed to analyze and answer questions from legal documents such as agreements, contracts, and policy PDFs.

The system retrieves relevant clauses from documents and generates **context-aware responses** using a local LLM. It also integrates a **Human-in-the-Loop (HITL)** mechanism for handling complex or ambiguous legal queries.

---

##  Features

* PDF-based legal document processing
*  Semantic search using embeddings
*  Context-aware answer generation
*  LangGraph-based workflow orchestration
*  Conditional routing (Answer vs Escalation)
*  Human-in-the-Loop (HITL) support
*  Fully offline setup using Ollama

---

## 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* ChromaDB
* Ollama (TinyLlama)

---

##  System Architecture

```
User Query
    ↓
Intent Routing
    ↓
Retrieval (ChromaDB)
    ↓
LLM Processing
    ↓
Decision Layer
    ↓
Answer  OR  HITL Escalation
```

---

## 📁 Project Structure

```
project/
│
├── data/                  # Legal PDFs (contracts, agreements)
├── embeddings/            # Vector database (ChromaDB)
│
├── src/
│   ├── ingest.py          # Document ingestion pipeline
│   ├── retriever.py       # Retrieval logic
│   ├── generator.py       # LLM response generation
│   ├── router.py          # Query routing logic
│   ├── graph.py           # LangGraph workflow
│   └── hitl.py            # Human-in-the-loop handling
│
├── docs/
│   ├── HLD.pdf
│   ├── LLD.pdf
│   └── Technical_Documentation.pdf
│
├── run_ingest.py          # Script to process and embed documents
├── app.py                 # Main application entry point
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install langchain langchain-community langgraph chromadb pypdf openai tiktoken
```

### 2️⃣ Start Ollama Server

```bash
ollama serve
```

### 3️⃣ Pull Required Model (if not already installed)

```bash
ollama pull tinyllama
```

### 4️⃣ Ingest Documents

```bash
python run_ingest.py
```

### 5️⃣ Run the Application

```bash
python app.py
```

---

## 💡 Notes

* Ensure your PDFs are placed inside the `data/` directory before ingestion.
* The embeddings will be stored locally in the `embeddings/` folder.
* The system runs fully offline once dependencies and models are set up.
* Used ollama tinyllama model in the current version due to hardware restriction (8GB RAM) if your system has better RAM(24GB+) with RTX 2050 and above i would suggest go go with better models like lamma3 for better results and minimal/null halucinations
* For systems with decent RAM utilizations (8GB+) use phi3 model which is better than tinylamma model as the parameters required is higher in this case
* This project runs LLM locally on the system, if you want to go with API rather than local LLM (ollama) i would suggest OpenAi,Gemini Apis'(Pay per credits used)

---

## 📄 License

This project is open-source and free to use for educational and research purposes.

---
