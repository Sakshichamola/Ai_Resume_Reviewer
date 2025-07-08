import streamlit as st
from resume_parser import extract_text_from_pdf, extract_entities
from job_matcher import match_skills

st.title("🧠 AI Resume Reviewer")

uploaded_resume = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

if uploaded_resume and job_description:
    with st.spinner("Analyzing your resume..."):
        text = extract_text_from_pdf(uploaded_resume)
        resume_skills = extract_entities(text)
        match_score = match_skills(resume_skills, job_description)
        
        st.subheader("🔍 Resume Skill Match Results")
        st.write(f"**Match Score:** {match_score} %")
        st.write(f"**Extracted Skills from Resume:**")
        st.write(", ".join(resume_skills))
