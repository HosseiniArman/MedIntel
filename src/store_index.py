import os
from langchain.vectorstores import Pinecone
from helper import load_data, text_split, download_huggingface_embedding

def create_index():
    """Loads medical data, processes it, and stores embeddings in Pinecone."""
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    if not PINECONE_API_KEY:
        raise ValueError("PINECONE_API_KEY is not set.")

    data_path = os.path.join(os.getcwd(), "data")
    data = load_data(data_path)
    text_chunks = text_split(data)
    embeddings = download_huggingface_embedding()

    Pinecone.from_documents(
        text_chunks,
        embedding=embeddings,
        index_name="medintel-index",
    )
    print("✅ Data successfully indexed in Pinecone.")

if __name__ == "__main__":
    create_index()

