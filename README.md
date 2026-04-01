******📊📄 Multi-Format Document AI Agent (PDF + CSV + Excel)******

This project is an AI-powered document assistant built using LangChain + Google Gemini (GenAI) that can intelligently process and answer queries from:

**📄 PDF files
📊 CSV files
📈 Excel files**

It automatically detects the file type and loads the appropriate agent to interact with your data.

🚀 Features
🔍 Smart File Detection
Automatically loads PDF or CSV/Excel agent based on file type
📄 PDF Question Answering
Uses embeddings + vector search (FAISS)
Retrieves relevant content and answers questions using LLM
📊 CSV/Excel Data Analysis
Supports .csv, .xlsx, .xls
Perform:
Data summary
Column listing
Top rows preview
Statistical analysis
🤖 LLM-Powered Responses
Uses Google Gemini (gemini-3-flash-preview) for intelligent answers
💬 Interactive CLI Chatbot
Ask questions continuously until exit

## FLOW
📂 Enter file path: sample.pdf

📄 PDF Agent Loaded

Ask something: What is this document about?
🤖: This document discusses...

Ask something: exit


## 🧠 Project Architecture

```mermaid
graph TD
    A[User Input] --> B[Enter File Path]
    B --> C{File Type Detection}

    C -->|PDF| D[PDF Agent]
    C -->|CSV/Excel| E[CSV/Excel Agent]

    D --> F[Load PDF]
    F --> G[Create Embeddings]
    G --> H[Store in FAISS]
    H --> I[Retrieve Context]
    I --> J[Gemini LLM]

    E --> K[Load Data using Pandas]
    K --> L[Process Query Logic]
    L --> J

    J --> M[Generate Response]
    M --> N[Display Output]



