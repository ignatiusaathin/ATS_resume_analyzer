# ATS_resume_analyzer

### PDF Extraction (pdf.py)
Purpose:
Reads uploaded resume
Extracts text
Stores in variable
This module converts resume PDF into plain text for AI processing.
### Resume Analysis Logic (analysis.py)

Core AI Logic:

model = genai.GenerativeModel('gemini-2.0-flash’)
AI Generates:
ATS Score
Good Fit Evaluation
SWOT Analysis
Selection Probability
Prompt engineering is used to instruct the model to generate structured bullet-point outputs.
### Streamlit Interface (interface.py)

User Interface:

File uploader
Job description input
Submit button
Results display
Streamlit connects frontend with backend functions seamlessly.
