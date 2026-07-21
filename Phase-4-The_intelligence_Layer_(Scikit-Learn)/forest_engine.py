import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Non-linear synthetic data (Now with edge cases/noise)
data = {
    'Age': [15, 16, 25, 28, 35, 45, 55, 65, 14, 22, 32, 42, 52, 62, 18, 29, 38, 48, 58, 70],
    'Income': [10000, 120000, 40000, 150000, 110000, 130000, 90000, 200000, 5000, 30000, 140000, 60000, 160000, 80000, 110000, 50000, 120000, 70000, 180000, 250000],
    'Bought_VR': [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0] # Added edge cases
}

df = pd.DataFrame(data)
print("--- Ensemble Voting Engine Online ---")

y = df["Bought_VR"]
X = df.drop("Bought_VR", axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=100)

model.fit(X_train,y_train)

predictions = model.predict(X_test)

print(predictions,"\n")
print(confusion_matrix(y_test,predictions),"\n")
print(classification_report(y_test,predictions))
