# Build-a-Simple-RAG-Application
Build a Simple RAG (Retrieval-Augmented Generation) application to query documents efficiently. Load PDFs, split text into chunks, and use a vector store to retrieve relevant information. Integrate a language model to generate precise answers from retrieved content.
📄 Paracetamol PDF QA System

A Streamlit web app that allows users to upload a PDF about Paracetamol and ask questions. Powered by LangChain, OpenAI embeddings, and FAISS for fast and accurate retrieval-augmented answers (RAG).

🚀 Features

Upload any PDF document about Paracetamol.

Automatically splits PDF text into chunks for better search.

Generates embeddings using OpenAI.

Retrieves and answers questions using a RAG pipeline.

Interactive web interface built with Streamlit.

🛠️ Technologies Used

Python 3.10+

Streamlit – Web app interface

LangChain – RAG framework

FAISS – Vector database for fast retrieval

OpenAI Embeddings – Converts text chunks into vectors

PyPDF2 – Reads PDF files

📦 Installation

Clone the repository:

git clone https://github.com/<your-username>/paracetamol-pdf-qa.git
cd paracetamol-pdf-qa

Install dependencies:

pip install -r requirements.txt

Example requirements.txt:

streamlit
langchain
faiss-cpu
PyPDF2
openai

Set your OpenAI API Key:

export OPENAI_API_KEY="your_api_key_here"    # Linux/Mac
setx OPENAI_API_KEY "your_api_key_here"      # Windows
🖥️ Running the App
streamlit run paracetamol.py

Upload a PDF file about Paracetamol.

Type a question in the input box.

Get answers retrieved from your PDF content.
