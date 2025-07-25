# 🧾 Portfolio Builder + Job Coach

An AI-powered Streamlit web app to help job seekers create polished professional assets including resumes, cover letters, LinkedIn summaries, and more — all using LLaMA3 via Ollama and LangChain.

---

## 🚀 Features

| Module                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| ✅ Resume Generator        | Create a professional, ATS-friendly resume in seconds                      |
| ✅ Cover Letter Generator  | Draft tailored and polished cover letters for any job                      |
| ✅ CV Analyzer             | Upload your resume (PDF) and get instant feedback & suggestions            |
| ✅ LinkedIn Summary Writer| Generate an engaging and professional LinkedIn bio                         |
| ✅ Mock Interview Chatbot  | Simulate job interviews with an AI career coach                            |

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — Frontend UI
- [LangChain](https://www.langchain.com/) — Prompt templates & chains
- [Ollama](https://ollama.com/) — Local LLaMA3 language model runtime
- [PyPDF](https://pypi.org/project/pypdf/) — PDF parsing (for resume upload)

---

## 📸 App Preview

![App Screenshot](https://via.placeholder.com/900x450.png?text=App+Screenshot+Preview)

> Replace with your actual screenshot or Streamlit Cloud link

---

## 💡 Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/portfolio-builder.git
cd portfolio-builder

Create and Activate Virtual Environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install Dependencies

pip install -r requirements.txt

📄 Requirements.txt

streamlit
langchain
langchain-community
pypdf


Install and Run Ollama

ollama pull llama3

Run the Streamlit App

streamlit run portfolio_builder_app.py

📁 Folder Structure

portfolio-builder/
├── cv_builder_app.py         # Main Streamlit application
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
└── .venv/                    # Virtual environment (excluded in .gitignore)

