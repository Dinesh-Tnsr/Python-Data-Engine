import json
import pandas as pd
import joblib

print("--- Factory IoT Server Online ---")
print("[SYS] Intercepting live network payload...")

# Simulated incoming API payload as JSON text
live_payload = """
{
    "sensor_id": "TURB-099",
    "timestamp": "2026-07-25T14:03:10Z",
    "telemetry": {
        "RPM": 18800,
        "Temperature_C": 112,
        "Vibration_hz": 125
    }
}
"""

# Parse JSON text into a Python dictionary
dic_payload = json.loads(live_payload)

# Scalar dict values become one row by wrapping in a list
df = pd.DataFrame([dic_payload["telemetry"]])

live_engine = joblib.load("turbine_engine.pkl")

predictions = live_engine.predict(df)

print(predictions,"\n")

if(predictions == 0):
    print("[OK] TURBINE STABLE")

else:
    print("[CRITICAL] INITIATE EMERGENCY SHUTDOWN")

