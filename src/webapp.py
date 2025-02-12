from flask import Flask, render_template, request, jsonify
import os
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from helper import download_huggingface_embedding

app = Flask(__name__)

# Load API Key for Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set.")

# Load embeddings and document store
embeddings = download_huggingface_embedding()
docsearch = Pinecone.from_existing_index("medintel-index", embeddings)

# Define Chatbot Prompt
prompt_template = """Use the provided medical knowledge base to generate accurate answers.
If the answer is not available, say 'I do not know'.
Context: {context}
User Question: {question}
Helpful answer:
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Initialize Language Model
config = {"max_new_tokens": 512, "temperature": 0.8}
llm = CTransformers(
    model="TheBloke/Llama-2-7B-Chat-GGML",
    model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config=config,
)

# Retrieval-Based QA System
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT},
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form["msg"]
    response = qa.invoke(user_message)
    return jsonify({"response": response["result"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

