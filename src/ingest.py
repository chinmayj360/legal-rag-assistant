from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddingss

def ingest_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="phi3")

    vectordb = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="embeddings/"
    )

    vectordb.persist()
    return vectordb