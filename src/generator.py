from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="tinyllama")

def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a legal assistant.
Answer ONLY using the context below.
Explain in simple terms.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content