# 📝 Summarization + QA Tool

This project is a **text summarization and question-answering tool** built with Python, Streamlit, and HuggingFace Transformers.  
It allows users to:  

- Summarize any text in **short, medium, or long** length.  
- Ask **multiple questions** about the generated summary in a loop-like interface.  
- View a **history of questions and answers** like a chat.

---

## ⚡ Features

- CPU-compatible (works without GPU)  
- Interactive Streamlit UI  
- Uses `facebook/bart-large-cnn` for summarization  
- Uses `deepset/roberta-base-squad2` for question-answering  
- Session-based QA history  

---

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <your-repo-folder>
Create a virtual environment:
python -m venv venv
Activate the virtual environment:

Windows:
venv\Scripts\activate


macOS / Linux:
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the app:
streamlit run app.py
```
🖼️ Screenshots
<img width="1396" height="777" alt="m1" src="https://github.com/user-attachments/assets/c18ddaec-6e2d-4fa0-a4c8-4e9521a37c20" />
<img width="1398" height="784" alt="m2" src="https://github.com/user-attachments/assets/0c894093-1074-4858-9ce6-46b56ab3f861" />

🛠️ Dependencies

streamlit

transformers

torch

langchain

langchain-huggingface

📌 Usage

Enter the text you want to summarize.

Select the summary length (short/medium/long).

Click Generate Summary.

Ask any questions about the summary in the input box.

Click Get Answer to see the response.

Repeat step 4 to ask multiple questions.

⚠️ Notes

The app downloads HuggingFace models automatically on first run.

CPU only is supported, GPU is optional.

Large text inputs may take some time to process on CPU.
