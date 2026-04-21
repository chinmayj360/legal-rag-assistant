from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def get_retriever():
    embeddings = OllamaEmbeddings(model="tinyllama")

    vectordb = Chroma(
        persist_directory="embeddings/",
        embedding_function=embeddings
    )

    return vectordb.as_retriever(search_kwargs={"k": 3})