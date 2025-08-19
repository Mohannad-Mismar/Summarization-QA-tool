import streamlit as st
from transformers import pipeline
from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

st.title("📝 Summarization + QA ")

@st.cache_resource
def init_pipelines():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
    refiner    = pipeline("summarization", model="facebook/bart-large", device=-1)
    qa         = pipeline("question-answering", model="deepset/roberta-base-squad2", device=-1)
    return summarizer, refiner, qa

summarizer, refiner, qa_pipeline = init_pipelines()

if "summary" not in st.session_state:
    st.session_state.summary = ""
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

text_to_summarize = st.text_area("Enter text to summarize:")
length = st.selectbox("Select summary length:", ["short", "medium", "long"])

if st.button("Generate Summary"):
    if text_to_summarize.strip():
        summary_step1 = summarizer(text_to_summarize, max_length=150, min_length=50, do_sample=False)
        summary_step2 = refiner(summary_step1[0]['summary_text'], max_length=150, min_length=50, do_sample=False)
        st.session_state.summary = summary_step2[0]['summary_text']
        st.session_state.qa_history = []  

if st.session_state.summary:
    st.subheader("🔹 Generated Summary")
    st.write(st.session_state.summary)

    question = st.text_input("Ask a question about the summary:")
    if st.button("Get Answer") and question.strip():
        answer = qa_pipeline(question=question, context=st.session_state.summary)
        st.session_state.qa_history.append({"question": question, "answer": answer["answer"]})

    if st.session_state.qa_history:
        st.subheader("💬 QA History")
        for qa in st.session_state.qa_history:
            st.markdown(f"**Q:** {qa['question']}")
            st.markdown(f"**A:** {qa['answer']}")
            st.write("---")
