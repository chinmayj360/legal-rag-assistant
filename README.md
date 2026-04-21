# ⚖️ Legal Document RAG Assistant (LangGraph + HITL)

##  Overview
This project is a Retrieval-Augmented Generation (RAG) system designed to analyze and answer questions from legal documents such as agreements, contracts, and policy PDFs.

The system retrieves relevant clauses from documents and generates context-aware responses using a local LLM. It also includes a Human-in-the-Loop (HITL) mechanism for complex or ambiguous legal queries.

---

##  Features
- 📄 PDF-based legal document processing
-  Semantic search using embeddings
-  Context-aware answer generation
-  LangGraph-based workflow system
-  Conditional routing (Answer vs Escalate)
-  Human-in-the-Loop escalation
-  Fully offline and free (Ollama)

---

## Tech Stack
- Python
- LangChain
- LangGraph
- ChromaDB
- Ollama (tinyllama)

---

## System Architecture

User Query  
→ Intent Routing  
→ Retrieval (ChromaDB)  
→ LLM Processing  
→ Decision Layer  
→ Answer OR HITL Escalation  

---

## 📂 Project Structure
project/
├── data/ # Legal PDFs (contracts, agreements)
├── embeddings/ # Vector database (ChromaDB)
├── src/
│ ├── ingest.py
│ ├── retriever.py
│ ├── generator.py
│ ├── router.py
│ ├── graph.py
│ └── hitl.py
├── docs/
│ ├── HLD.pdf
│ ├── LLD.pdf
│ ├── Technical_Documentation.pdf
├── run_ingest.py
├── app.py
└── README.md


---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install langchain langchain-community langgraph chromadb pypdf openai tiktoken

### 2. Start ollama
```bash
ollama serve

### 3.Ingest document
```bash
python run_ingest.py

### 4. run application
```bash
python app.py
