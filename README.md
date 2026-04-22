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
pip install sentence-transformers
```

### 2️⃣ Set Groq API Key

```bash
 $env:GROQ_API_KEY="your_key_here"
```

### 3️⃣ Ingest Documents

```bash
python run_ingest.py
```

### 4️⃣ Run the Application

```bash
    python app.py
```


---
##Notes

*Ensure your PDFs are placed inside the data/ directory before ingestion.
*The embeddings are stored locally in the embeddings/ folder.
*This project uses HuggingFace embeddings (all-MiniLM-L6-v2) for retrieval.
*The LLM is powered via Groq API using llama-3.3-70b-versatile, providing fast and high-quality responses.
*Compared to local models, API-based LLMs:
*Provide significantly better reasoning
*Reduce hallucinations
*Do not depend on system RAM/GPU
*Ensure your API key is set before running the application.

---

## 📄 License

This project is open-source and free to use for educational and research purposes.

---
