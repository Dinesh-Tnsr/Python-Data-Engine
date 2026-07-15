import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data: Hours Studied, Pointer Errors Fixed, Exam Result (1=Pass, 0=Fail)
data = {
    'Hours_Studied': [2, 10, 3, 8, 1, 12, 5, 9, 4, 11],
    'Pointer_Errors': [15, 2, 10, 4, 20, 1, 8, 3, 12, 0],
    'Passed': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
print("--- Binary Classification Engine Online ---")

y = df["Passed"]
X = df.drop("Passed", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled,y_train)
prediction = model.predict(X_test_scaled)

print(prediction)
print("\n")
print(y_test)
print("\n")
print(accuracy_score(y_test,prediction))
