import streamlit as st
from pdf_process import get_text_from_resume
from interview_session import create_question_from_context, evaluate_answer

st.set_page_config(page_title="Virtual AI Interviewer", page_icon="🎯")
st.markdown("## 🎤 AI-Powered Interview Simulator")

st.markdown("### 📁 Step 1: Upload Your Resume")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = get_text_from_resume("uploaded_resume.pdf")

    st.markdown("---")
    st.markdown("### 🧾 Resume Overview")
    st.code(resume_text, language="text")

    if "context" not in st.session_state:
        st.session_state.context = resume_text

    st.markdown("---")
    st.markdown("### 🛠️ Step 2: Generate a Question")

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("🎲 Ask Me a Question"):
            st.session_state.question = create_question_from_context(st.session_state.context)

    if "question" in st.session_state:
        with col2:
            st.success("🎯 Interview Question Ready!")
            st.markdown(f"**🧠 {st.session_state.question}**")

        st.markdown("### ✍️ Step 3: Type Your Answer")
        answer = st.text_area("📌 Your Response")

        if st.button("📤 Submit for Evaluation"):
            score = evaluate_answer(st.session_state.question, answer)
            st.balloons()
            st.markdown(f"### 🏆 Score: **{score}/10**")
            st.info("📈 Keep practicing to improve your interview performance!")

else:
    st.warning("📄 Please upload your resume to get started.")
