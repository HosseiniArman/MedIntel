from setuptools import find_packages, setup

setup(
    name="MedIntel",
    version="1.0.0",
    description="A Retrieval-Augmented Medical Chatbot using Llama-2 and Pinecone for vector search.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask",
        "langchain",
        "pinecone-client",
        "sentence-transformers",
        "transformers",
        "tqdm",
    ],
    python_requires=">=3.8",
)

