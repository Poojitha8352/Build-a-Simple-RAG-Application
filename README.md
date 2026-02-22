# Build-a-Simple-RAG-Application
Build a Simple RAG (Retrieval-Augmented Generation) application to query documents efficiently. Load PDFs, split text into chunks, and use a vector store to retrieve relevant information. Integrate a language model to generate precise answers from retrieved content.
📄 Paracetamol PDF QA System

An AI-powered PDF Question-Answering web app built with Streamlit and LangChain that allows users to upload a PDF about Paracetamol and get instant answers.

🌟 Key Highlights

Interactive PDF Upload: Users can upload any PDF about Paracetamol.

Smart Text Splitting: Automatically splits text into manageable chunks.

AI-Powered Retrieval: Uses OpenAI embeddings + FAISS vector database for fast and accurate answers.

User-Friendly Interface: Built with Streamlit for an easy-to-use web experience.

RAG Pipeline: Retrieval-Augmented Generation ensures answers are contextually relevant.

🛠️ Technologies Used

Python 3.10+

Streamlit – Interactive web app

LangChain – RAG framework for AI pipelines

FAISS – Efficient vector database for retrieval

OpenAI Embeddings – Converts text chunks to vector representations

PyPDF2 – PDF text extraction

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
🖥️ How to Run
streamlit run paracetamol.py

Upload your PDF about Paracetamol.

Ask any question in the input box.

Get accurate, context-aware answers instantly.

🧩 Project Structure
paracetamol-pdf-qa/
│
├─ paracetamol.py       # Main Streamlit application
├─ requirements.txt     # Dependencies
├─ README.md            # Project documentation
└─ sample_pdfs/         # Optional sample PDF files
⚡ Future Improvements

Support multiple PDF uploads at once.

Advanced prompts for more natural answers.

Downloadable answers or summaries.

Enhanced UI with multi-tab support for different sections.
