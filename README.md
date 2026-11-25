# CampusGPT – AI-Powered University Student Assistant

## Project Overview

CampusGPT is an AI-powered university student assistant developed using Generative AI and Large Language Models (LLMs). It helps students with academic learning, university-related queries, placement preparation, resume analysis, and interview practice through an interactive chatbot interface.

The application uses the Groq LLM API to generate intelligent responses and a basic Retrieval-Augmented Generation (RAG) approach to retrieve relevant information from university knowledge files and uploaded PDF documents.

## Objectives

- Provide students with an AI-powered academic assistant.
- Answer university-related questions using available knowledge documents.
- Simplify complex academic topics.
- Generate exam-oriented answers and study notes.
- Assist students with resume analysis and placement preparation.
- Support aptitude practice and mock interview preparation.

## Key Features

### 1. University Assistant
- Answers university-related questions.
- Uses university FAQ and uploaded PDF content as reference.
- Retrieves relevant context using keyword-based retrieval.

### 2. Study Assistant
- Provides simple explanations.
- Generates 5-mark and 10-mark answers.
- Creates short notes.
- Suggests important practice questions.

### 3. Placement Assistant
- Provides career and placement guidance.
- Analyzes uploaded resumes.
- Identifies skills, strengths, and areas for improvement.
- Provides suggestions for improving resume content.

### 4. Aptitude and Mock Interview Assistant
- Supports quantitative aptitude practice.
- Helps with logical reasoning and verbal ability.
- Provides Java, Python, and SQL interview preparation.
- Supports HR interview practice.

### 5. PDF Document Support
- Allows users to upload PDF documents.
- Extracts text from uploaded PDFs.
- Uses extracted content to provide context-aware responses.

### 6. Conversation Memory
- Maintains conversation history during the current application session.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | User interface |
| Groq API | LLM integration |
| GPT-OSS 120B | Language model |
| PyPDF | PDF text extraction |
| Python-dotenv | Environment variable management |
| Basic RAG | Knowledge retrieval |

## System Requirements

- Windows, Linux, or macOS
- Python 3.12 or compatible version
- VS Code or another Python IDE
- Internet connection
- Groq API key

## Project Structure

```text
CampusGPT/
│
├── app.py
├── rag_engine.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── university_faq.txt
│
└── README.md
```

## Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/kuruvarohini2004-creator/CampusGPT-University-Assistant.git
```

### Step 2: Open the project folder

```bash
