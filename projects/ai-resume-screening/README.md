# 🤖 AI Resume Screening & Job Matching

A practical NLP project that compares a resume with a job description and produces a similarity score.

## 🧠 Concept

```text
Resume ─┐
        ├→ Text Cleaning → TF-IDF → Cosine Similarity → Match Score
Job ────┘
```

## 🐍 Core Python

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "Python SQL machine learning pandas scikit-learn data analysis"
job = "Python SQL machine learning data analytics scikit-learn"

vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform([resume, job])
score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

print(f"Resume-job similarity: {score:.2%}")
```

## 🛠️ Stack

Python • NLP • TF-IDF • Cosine Similarity • Scikit-learn

> This project is a matching aid, not an automated hiring decision system.
