from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def generate_answer(query, docs):
    docs = docs[:3]

    context = "\n\n".join([
        doc.page_content.strip().replace("\n", " ")
        for doc in docs
    ])

    prompt = f"""
You are a legal document assistant.

STRICT RULES:
- Answer ONLY using the provided context
- Do NOT make up information
- If answer is not found, say: Not found in document
- Keep answer short and clear

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content