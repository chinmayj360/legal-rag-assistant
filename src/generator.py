from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="tinyllama")

def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a legal document assistant.

STRICT RULES:
- Answer ONLY using the provided context
- Do NOT make up information
- If answer is not found, say: "Not found in document"
- Keep answer simple and clear

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content