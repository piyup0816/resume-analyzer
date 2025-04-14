import streamlit as st
import openai
import PyPDF2
import docx

openai.api_key = "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"

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
job_role = st.text_input("Enter Desired Job Role:")

if st.button("Analyze Resume"):
    if uploaded_file and job_role:
        with st.spinner("Analyzing your resume..."):
            # Read file content
            if uploaded_file.name.endswith(".pdf"):
                resume_text = read_pdf(uploaded_file)
            else:
                resume_text = read_docx(uploaded_file)

            # Generate prompt
            prompt = (
                f"Analyze this resume for the job role: {job_role}.\n\n"
                f"Resume:\n{resume_text}\n\n"
                f"Give feedback, strengths, and improvement suggestions."
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            analysis = response['choices'][0]['message']['content']

            st.subheader("🧠 Resume Analysis:")
            st.write(analysis)
    else:
        st.warning("Please upload a resume and enter a job role.")
