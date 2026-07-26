import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

# Synthetic Data: Fraud Detection (1=Fraud, 0=Legit)
data = {
    'Amount_Transferred': [50, 15000, 25, 12000, 100, 80, 14000, 45, 11000, 60],
    'Account_Age_Days':   [365, 2, 800, 1, 400, 500, 5, 750, 10, 600],
    'Is_Fraud':           [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print("--- Production Pipeline Engine Online ---")

y = df["Is_Fraud"]
X = df.drop("Is_Fraud", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

prod_pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('ai',LogisticRegression())
])

prod_pipeline.fit(X_train,y_train)

predictions = prod_pipeline.predict(X_test)

print(predictions,"\n")
print(classification_report(y_test,predictions))