import os
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Model name
model_name = "models/gemini-2.0-flash"

# Function to extract text from PDF
def extract_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


# Function to analyze resume
def analyze_resume(pdf_file, job_description):

    resume_text = extract_pdf_text(pdf_file)

    prompt = f"""
    You are an ATS (Applicant Tracking System).

    Compare the following Resume and Job Description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide:

    1. ATS Score (0-100)
    2. Missing Keywords
    3. Good Fit Analysis
    4. SWOT Analysis
    5. Probability of Selection (%)
    6. Suggestions to improve resume

    Format response clearly with headings and bullet points.
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.text


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="ATS Resume Analyzer", page_icon="📄")

st.title("📄 ATS Resume Analyzer using Gemini AI")

st.write("Upload your resume and paste the job description to check ATS compatibility.")

uploaded_pdf = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_pdf is None:
        st.warning("Please upload a resume PDF")

    elif job_description == "":
        st.warning("Please enter a Job Description")

    else:
        with st.spinner("Analyzing Resume..."):
            result = analyze_resume(uploaded_pdf, job_description)

        st.success("Analysis Completed")

        st.markdown(result)