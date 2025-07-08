from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_skills(resume_skills, jd_text):
    jd_vectorizer = TfidfVectorizer()
    all_text = [' '.join(resume_skills), jd_text]
    tfidf_matrix = jd_vectorizer.fit_transform(all_text)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)
