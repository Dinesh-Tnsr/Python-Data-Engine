import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Server Telemetry Data (20 records)
# CPU_Temp (C), RAM_Usage (GB), Disk_IO (MB/s), Crash (1=Yes, 0=No)
data = {
    'CPU_Temp': [45, 88, 50, 92, 48, 85, 42, 95, 55, 90, 47, 89, 52, 93, 49, 87, 44, 96, 51, 91],
    'RAM_Usage': [16, 62, 18, 64, 15, 60, 14, 65, 17, 61, 16, 63, 19, 66, 15, 59, 14, 64, 18, 62],
    'Disk_IO': [120, 800, 150, 850, 110, 780, 105, 900, 130, 820, 115, 810, 140, 880, 125, 790, 110, 920, 135, 830],
    'Crash': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
print("--- Enterprise Telemetry Engine Online ---")

y = df["Crash"]
X = df.drop("Crash", axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train_scaled,y_train)
predictions = model.predict(X_test_scaled)

print("predictions:",predictions,"\n")

matrix = confusion_matrix(y_test,predictions)

print(matrix,"\n")

report = classification_report(y_test,predictions)
print(report)
