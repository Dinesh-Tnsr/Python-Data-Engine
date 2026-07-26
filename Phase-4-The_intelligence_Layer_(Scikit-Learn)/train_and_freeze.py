import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Synthetic Data: Fraud Detection
data = {
    'Amount': [50, 15000, 25, 12000, 100, 80, 14000, 45, 11000, 60],
    'Age':    [365, 2, 800, 1, 400, 500, 5, 750, 10, 600],
    'Fraud':  [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

print("--- AI Training Facility Online ---")

y = df["Fraud"]
X = df.drop("Fraud", axis=1)

# Build and Train the Unbreakable Object
prod_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('ai', LogisticRegression(random_state=42))
])
prod_pipeline.fit(X, y)
print("[SYS] Pipeline trained successfully on all data.")

joblib.dump(prod_pipeline,"fraud_engine.pkl")

print("[SYS] Engine frozen and saved to disk.")