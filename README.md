
# Resume Screening AI

## Project Description
This project automates the process of screening and ranking resumes for Data Science roles using Natural Language Processing (NLP) techniques. It extracts text from resumes (PDF/DOCX), preprocesses and cleans the data, filters by category, and ranks candidates based on their relevance to a provided job description.

## Key Features & Workflow
1. **Resume Extraction**
   - **PDF & DOCX Support:** Uses pdfminer.six for PDFs and python-docx for DOCX files.
   - **Batch Processing:** Scans a folder for resume files, extracts text, and stores filename, text, and inferred category.
   - **CSV Import:** Optionally processes resumes from a CSV file for quick inspection.
2. **Text Preprocessing**
   - **Cleaning:** Converts text to lowercase, removes non-alphabetic characters, extra spaces, and common section headers (like "Education", "Skills", etc.).
   - **Stopword Removal:** Uses NLTK to remove common English stopwords, improving the quality of text analysis.
3. **Category Filtering**
   - **Data Science Focus:** Filters resumes by category (e.g., "Data Science") using filename patterns or CSV data, ensuring only relevant candidates are considered.
4. **Advanced Scoring & Ranking**
   - **TF-IDF Vectorization:** Converts resume and job description text into numerical vectors using scikit-learn’s TfidfVectorizer.
   - **Cosine Similarity:** Measures how closely each resume matches the job description.
   - **Keyword Boosting:** Increases the score for resumes containing important keywords from the job description.
   - **Section Weighting:** Gives extra weight to critical sections like "Skills" and "Experience".
   - **Synonym Handling:** Recognizes simple synonyms (e.g., "python" and "py") to improve matching.
   - **Combined Score:** Ranks resumes using a weighted combination of similarity and keyword match.
5. **Output & Reporting**
   - **Top Matches:** Displays the top-ranked resumes for the Data Science category, including filenames and scores.
   - **Progress Messages:** Prints clear status updates and error messages for each step.

## Technologies Used
- Python 3
- pdfminer.six (PDF extraction)
- python-docx (DOCX extraction)
- pandas (CSV processing)
- scikit-learn (TF-IDF, cosine similarity)
- NLTK (stopword removal)
- Regular Expressions (text cleaning, category extraction)

## How It Works (Step-by-Step)
1. Extract resumes from a folder or CSV.
2. Preprocess the text (clean, normalize, remove stopwords).
3. Filter resumes by category (e.g., Data Science).
4. Read the job description from a text file.
5. Score and rank resumes using advanced NLP techniques.
6. Display the top matching candidates.

## Why Is This Useful?
- Saves recruiter time by automating resume screening.
- Improves accuracy by using advanced text analysis.
- Customizable for different job categories and requirements.

## How to Run
1. Place your resumes in the `resumes` folder (PDF/DOCX).
2. Add a job description in `job_description.txt`.
3. Run the script:
   ```bash
   python main.py
   ```
4. View the ranked results in your terminal.

## Example Output
```
Top matching resumes (Data Science):
1. Sakshi_Resume.pdf - Score: 0.812
2. Sinjini_Resume.docx - Score: 0.798
...
Ranking complete! 🎉
```

## Repository Setup
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Sakshi-ctrl-debug/Resume-Screening-Ai
git push -u origin main
```

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Please see the LICENSE file in the repository for the full text.

