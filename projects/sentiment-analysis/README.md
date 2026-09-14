# 💬 NLP Sentiment Analysis API

A lightweight NLP classification API that predicts whether text is positive or negative.

## 🔄 Flow

`Text → TF-IDF → Logistic Regression → Sentiment API`

## 🚀 Endpoint

```http
POST /predict
Content-Type: application/json
```

```json
{"text":"The service was amazing"}
```

Response:

```json
{"sentiment":"positive"}
```

## 🛠️ Stack

Python • Flask • Scikit-learn • NLP • TF-IDF

> The included corpus is intentionally tiny for demonstration. A real project should train on a properly prepared labeled dataset.
