# 📰 Hybrid Fake News Detector

An AI-powered news verification project combining NLP, deep learning, and real-time claim validation.

## ✨ Features

- TF-IDF based text representation
- LSTM + CNN hybrid classification architecture
- Google Gemini AI assisted claim verification
- GNews API based real-time news validation
- End-to-end prediction workflow

## 🧠 Architecture

```text
News / Claim
     ↓
Text Cleaning
     ↓
TF-IDF Features
     ↓
LSTM + CNN Model
     ↓
Prediction
     ↓
Gemini Claim Verification
     ↓
GNews Real-Time Validation
     ↓
Final Verification Result
```

## 🧪 Example Python

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

texts = [
    "Scientists publish a new climate study",
    "Celebrity discovers impossible miracle cure"
]
labels = [1, 0]

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

prediction = model.predict(vectorizer.transform(["New research is published today"]))
print("Prediction:", prediction[0])
```

> This repository contains an educational implementation of the core NLP workflow. API keys must be stored in environment variables and never committed to Git.

## 🛠️ Stack

Python • TensorFlow/Keras • Scikit-learn • NLP • Gemini API • GNews API
