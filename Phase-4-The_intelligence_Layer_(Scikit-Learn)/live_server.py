import pandas as pd
import joblib

print("--- Bank Web Server Online ---")
print("[SYS] Receiving live API request...")

# The live data payload from the website
live_request = pd.DataFrame({
    'Amount': [13500],
    'Age':    [3]
})

live_engine = joblib.load("fraud_engine.pkl")
predictions = live_engine.predict(live_request)

print(predictions)