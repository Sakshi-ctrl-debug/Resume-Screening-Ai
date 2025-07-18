import os
from pdfminer.high_level import extract_text
from docx import Document
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return ""

def extract_all_resumes(resume_folder):
    resumes = []
    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)
        if filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.lower().endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            continue
        # Try to extract category from filename (e.g., DataScience_JohnDoe.pdf)
        category = None
        match = re.search(r'(data\s*science|machine\s*learning|ai|ml|analytics)', filename, re.IGNORECASE)
        if match:
            category = match.group(1).strip().lower()
        resumes.append({'filename': filename, 'text': text, 'category': category})
    return resumes

def process_resumes_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    for idx, row in df.iterrows():
        category = row['Category']
        resume_text = row['Resume']
        print(f"Category: {category}")
        print(f"Resume (first 300 chars): {resume_text[:300]}")
        print('-' * 40)

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove common section headers
    text = re.sub(r'(education|experience|skills|projects|summary|certifications|objective)', '', text)
    return text

# Download NLTK stopwords if not already present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stop_words])

def get_job_description(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def compute_similarity(resume_texts, job_desc):
    # Advanced scoring: TF-IDF + keyword boosting + section weighting
    from sklearn.metrics.pairwise import cosine_similarity
    # Extract keywords from job description
    keywords = set(job_desc.split())
    # Synonym handling (simple)
    synonyms = {'python': ['py'], 'machine': ['ml'], 'data': ['analytics']}
    def boost_keywords(text):
        for kw in keywords:
            if kw in text:
                text += (' ' + kw) * 2  # boost
            # Add synonyms
            for syn, syns in synonyms.items():
                if syn in text:
                    for s in syns:
                        text += (' ' + s)
        return text
    # Section weighting (simple)
    def weight_sections(text):
        weights = {'experience': 2, 'skills': 2, 'education': 1}
        for section, w in weights.items():
            if section in text:
                text += (' ' + section) * w
        return text
    # Apply boosting and weighting
    resume_texts_boosted = [weight_sections(boost_keywords(t)) for t in resume_texts]
    job_desc_boosted = weight_sections(boost_keywords(job_desc))
    all_texts = [job_desc_boosted] + resume_texts_boosted
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    scores = cosine_similarity(resume_vecs, job_vec)
    # Add keyword match score
    def keyword_score(text):
        return sum(1 for kw in keywords if kw in text)
    keyword_scores = [keyword_score(t) for t in resume_texts]
    # Combine scores (weighted)
    final_scores = [0.8 * s + 0.2 * (ks / (len(keywords) + 1)) for s, ks in zip(scores.flatten(), keyword_scores)]
    return final_scores

if __name__ == "__main__":
    # Process resumes from CSV
    process_resumes_from_csv('data/resumes.csv')
    print("CSV processing complete! 🎉")
    # Extract resumes from folder
    resume_folder = 'resumes'
    resumes = extract_all_resumes(resume_folder)
    if not resumes:
        print(f"No resumes found in folder '{resume_folder}' or extraction failed. Please check the folder and file formats.")
    else:
        # Filter resumes by Data Science category if available in the resume dict
        filtered_resumes = []
        for r in resumes:
            if 'category' in r and r['category']:
                if r['category'].strip().lower() == 'data science':
                    filtered_resumes.append(r)
            else:
                filtered_resumes.append(r)  # fallback if no category info
        if not filtered_resumes:
            print("No resumes found for category 'Data Science'.")
        else:
            job_desc = get_job_description('job_description.txt')
            job_desc_clean = remove_stopwords(preprocess_text(job_desc))
            resume_texts = [remove_stopwords(preprocess_text(r['text'])) for r in filtered_resumes]
            if not resume_texts or all(not t for t in resume_texts):
                print("No valid resume text extracted. Please check the resume files.")
            else:
                scores = compute_similarity(resume_texts, job_desc_clean)
                ranked = sorted(zip(filtered_resumes, scores), key=lambda x: x[1], reverse=True)
                print("\nTop matching resumes (Data Science):")
                for i, (resume, score) in enumerate(ranked[:10], 1):
                    print(f"{i}. {resume['filename']} - Score: {score:.3f}")
                print("\nRanking complete! 🎉")
