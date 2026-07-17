import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

# Simulated Deployment Results:
# 0 = Legitimate Transaction, 1 = Fraud
# Out of 15 transactions, 13 were legit, 2 were actual fraud.
y_test =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

# Our AI predicted these outcomes:
# It successfully caught one fraud, missed the other, and accidentally flagged a legit transaction.
predictions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]

print("--- Fraud Detection Audit Engine Online ---")

matrix = confusion_matrix(y_test,predictions)
print(matrix,"\n")

report = classification_report(y_test,predictions)
print(report)