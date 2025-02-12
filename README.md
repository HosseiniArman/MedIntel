# **MedIntel - AI-Powered Medical Chatbot with RAG**

### **An Intelligent, Retrieval-Augmented Generation (RAG)-Based Medical Chatbot Using Llama-2**

## 🌟 **Overview**
MedIntel is a state-of-the-art **Retrieval-Augmented Generation (RAG)** medical chatbot powered by **Llama-2**. It intelligently answers medical questions by retrieving knowledge from a curated database of trusted medical literature.

## 🏆 **Features**
✅ **Retrieval-Augmented Generation (RAG)** - Retrieves relevant medical documents before generating responses.  
✅ **Llama-2-Based Chatbot** - Uses the latest LLM technology for high-quality, context-aware answers.  
✅ **Efficient Vector Search** - Utilizes **Pinecone** for fast and scalable semantic search.  
✅ **Interactive Web Interface** - Flask-based web UI for a smooth chatbot experience.  
✅ **Modular & Extensible** - Easily adaptable for new medical datasets and use cases.  

---

## 🏗 **Project Structure**
```
MedIntel/
│── src/                   # Core backend logic
│   ├── webapp.py          # Flask web app
│   ├── helper.py          # Embeddings, data handling
│   ├── store_index.py     # Pinecone vector database setup
│── static/                # UI Styles
│   ├── style.css          # Chatbot UI styles
│── templates/             # Web App UI
│   ├── chat.html          # Chatbot front-end
│── data/                  # Knowledge source files
│── README.md              # Documentation
│── requirements.txt       # Dependencies
│── setup.py               # Project setup
│── .gitignore             # Ignore unnecessary files
│── LICENSE                # Open-source license
```

---

## ⚡ **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/MedIntel.git
cd MedIntel
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Pinecone API Key**
1. Create an account on [Pinecone.io](https://www.pinecone.io/)
2. Copy your API key and run:
```bash
export PINECONE_API_KEY="your_api_key_here"
```

### **5️⃣ Run the Chatbot**
```bash
python webapp.py
```
Access the chatbot at: **`http://localhost:8080/`**

---

## 📡 **How MedIntel Works**
1️⃣ **User inputs a medical question.**  
2️⃣ **Retriever fetches relevant knowledge.**  
3️⃣ **Llama-2 generates a response using retrieved context.**  
4️⃣ **The chatbot provides an accurate answer.**  

---

## 🛠 **Customization & Future Improvements**
- 🔹 **Fine-tuning Llama-2** for medical applications.
- 🔹 **Expanding the knowledge base** with more medical literature.
- 🔹 **Multilingual support** for global accessibility.

---

## 🎯 **Contributions & Support**
🔸 Feel free to **fork, star, and contribute**!  
🔸 For any questions, open an **issue** or reach out via **email**.

---


