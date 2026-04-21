from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

def get_retriever():
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="embeddings/",
        embedding_function=embeddings
    )

    return vectordb.as_retriever(search_kwargs={"k": 3})