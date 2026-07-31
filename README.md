# 📄 Longform Data Analyzer

An AI-powered document analysis tool that extracts knowledge and generates summaries from long documents using a local Large Language Model.

## 🚀 Features

- Upload and analyze long documents
- Extract key information:
  - People
  - Places
  - Dates
  - Numbers
  - Events
- Generate short document summaries
- Fixed-size document chunking strategy
- Runs locally using Ollama and Phi-3 Mini
- Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- Phi-3 Mini
- LangChain
- PyPDF

## 🧠 How It Works

1. User uploads a document.
2. The document is loaded and converted into text.
3. The text is split into smaller chunks using a fixed-size splitting strategy.
4. The chunks are analyzed by a local AI model.
5. Important facts are extracted.
6. A summary of the document is generated.

## 📂 Project Structure
