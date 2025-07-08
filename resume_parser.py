import PyPDF2
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_entities(text):
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'SKILL', 'PRODUCT', 'WORK_OF_ART']:
            skills.append(ent.text.lower())
    return list(set(skills))
