import os
from pdfminer.high_level import extract_text
from docx import Document


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return '\n'.join([para.text for para in doc.paragraphs])


def extract_resume_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError('Unsupported file type: ' + ext)


def keyword_match(resume_text, keywords):
    found = [kw for kw in keywords if kw.lower() in resume_text.lower()]
    return found


if __name__ == "__main__":
    # Example usage
    resume_path = os.path.join('data', 'sample_resume.pdf')  # Place a sample file here
    keywords = ['python', 'machine learning', 'nlp']
    try:
        text = extract_resume_text(resume_path)
        print('Extracted text (first 500 chars):')
        print(text[:500])
        print('\nMatched keywords:', keyword_match(text, keywords))
    except Exception as e:
        print('Error:', e)
