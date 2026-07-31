import streamlit as st
import tempfile
import os

from src.document_loader import load_document
from src.splitter import split_text
from src.extractor import extract_facts
from src.summarizer import summarize_text


st.set_page_config(
    page_title="Longform Data Analyzer",
    page_icon="📄"
)

st.title("📄 Longform Data Analyzer")
st.write(
    "Upload a long document and extract knowledge using a local AI model."
)


uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "txt"]
)


if uploaded_file:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_file.name)[1]
    ) as temp_file:

        temp_file.write(uploaded_file.read())
        file_path = temp_file.name


    st.success("Document uploaded successfully!")

    if st.button("Analyze Document"):

        with st.spinner("Reading document..."):

            text = load_document(file_path)


        st.subheader("📌 Document Preview")
        st.write(text[:1000])


        with st.spinner("Splitting document..."):

            chunks = split_text(text)


        st.info(
            f"Document split into {len(chunks)} chunks."
        )


        with st.spinner("Extracting knowledge using Phi-3..."):

            facts = extract_facts(chunks[0])


        st.subheader("🧠 Extracted Facts")

        st.write(facts)


        with st.spinner("Generating summary..."):

            summary = summarize_text(text)


        st.subheader("📝 Summary")

        st.write(summary)