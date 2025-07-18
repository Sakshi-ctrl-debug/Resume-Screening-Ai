<<<<<<< HEAD
# Resume Screening AI

Automated resume extraction, processing, and ranking for Data Science roles using NLP techniques.

## Features
- Extracts text from PDF and DOCX resumes
- Preprocesses and cleans resume/job description text
- Filters resumes by category (e.g., Data Science)
- Ranks resumes using TF-IDF, keyword boosting, section weighting, and synonym handling
- Displays top matching resumes

## Technologies
- Python 3
- pdfminer.six
- python-docx
- pandas
- scikit-learn
- nltk

## How to Use
1. Place resumes in the `resumes/` folder (PDF/DOCX format)
2. Add a job description in `job_description.txt`
3. Run the script:
   ```bash
   python main.py
   ```
4. View ranked results in the terminal

## How It Works
- Extracts and preprocesses resume/job description text
- Filters resumes by category
- Scores and ranks resumes using advanced NLP
- Shows top matches for the job description

## Example Output
```
Top matching resumes (Data Science):
1. JohnDoe.pdf - Score: 0.812
2. JaneSmith.docx - Score: 0.798
...
Ranking complete! 🎉
```

## Repository Setup
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

## License
MIT
=======
# Resume-Screening-Ai
>>>>>>> 062b61de638f4680b367aaed9e1ba8935b87dde9
