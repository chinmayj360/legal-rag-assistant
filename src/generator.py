from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0)

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