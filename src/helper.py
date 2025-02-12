import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_data(data_path: str):
    """Loads medical knowledge data from PDF documents."""
    loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()

def text_split(data):
    """Splits documents into smaller text chunks for efficient retrieval."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(data)

def download_huggingface_embedding():
    """Downloads and initializes Hugging Face embeddings for vector search."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

