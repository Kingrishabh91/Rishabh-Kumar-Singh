"""Unsupervised anomaly detection with Isolation Forest."""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Example numeric observations: [transaction_amount, transaction_count]
X = np.array([
    [120, 2], [150, 3], [95, 2], [180, 4],
    [130, 2], [110, 3], [5000, 1]
])

pipeline = make_pipeline(
    StandardScaler(),
    IsolationForest(contamination=0.1, random_state=42)
)

labels = pipeline.fit_predict(X)
for row, label in zip(X, labels):
    status = "ANOMALY" if label == -1 else "NORMAL"
    print(row, status)
