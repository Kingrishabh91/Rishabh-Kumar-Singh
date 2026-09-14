"""Customer churn prediction starter using scikit-learn."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Expected columns: tenure, monthly_charges, contract, target_churn
# df = pd.read_csv("data/customers.csv")

# Example usage after loading your dataset:
# X = df.drop(columns=["target_churn"])
# y = df["target_churn"]
# numeric = ["tenure", "monthly_charges"]
# categorical = ["contract"]
#
# preprocessor = ColumnTransformer([
#     ("num", Pipeline([
#         ("imputer", SimpleImputer(strategy="median")),
#         ("scaler", StandardScaler())
#     ]), numeric),
#     ("cat", Pipeline([
#         ("imputer", SimpleImputer(strategy="most_frequent")),
#         ("onehot", OneHotEncoder(handle_unknown="ignore"))
#     ]), categorical)
# ])
#
# model = Pipeline([
#     ("preprocess", preprocessor),
#     ("classifier", LogisticRegression(max_iter=1000))
# ])
#
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )
# model.fit(X_train, y_train)
# print(classification_report(y_test, model.predict(X_test)))

print("Load your customer dataset and uncomment the training workflow above.")
