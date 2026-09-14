"""Simple NLP sentiment-analysis API."""
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Small demonstration corpus. Replace with a larger labeled dataset in production.
texts = ["I love this product", "This is excellent", "I hate this", "Terrible experience"]
labels = ["positive", "positive", "negative", "negative"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)
model = LogisticRegression().fit(X, labels)

@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("text", "")).strip()
    if not text:
        return jsonify({"error": "text is required"}), 400

    prediction = model.predict(vectorizer.transform([text]))[0]
    return jsonify({"sentiment": prediction})

if __name__ == "__main__":
    app.run(debug=True)
