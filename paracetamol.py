import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import tempfile

st.set_page_config(page_title="Paracetamol PDF QA", layout="wide")
st.title("📄 RAG Question Answering System")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:

    # Save PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    st.success("PDF Uploaded Successfully ✅")

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split PDF into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Create embeddings for retrieval
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # ✅ Use Flan-T5 with text-generation pipeline
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    hf_pipeline = pipeline(
        task="text-generation",  # Use "text-generation", not "text2text-generation"
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=150,
        do_sample=False,
        temperature=0.7
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    # Prompt strictly using context
    prompt_template = """
You are a helpful medical assistant.
Answer the question based only on the context below.
Give 1–2 short, relevant sentences.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{question}

Answer:
"""

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
        chain_type_kwargs={"prompt": PROMPT}
    )

    query = st.text_input("Ask a question from the PDF:")

    if query:
        with st.spinner("Generating answer..."):
            result = qa_chain({"query": query})
            answer = result["result"].strip()
        st.write("### Answer:")
        st.write(answer)