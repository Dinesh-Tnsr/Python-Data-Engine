import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Historical Turbine Data
# RPM, Temperature_C, Vibration_hz, Failure (1=Yes, 0=No)
data = {
    'RPM': [15000, 18000, 15500, 19000, 14000, 18500, 16000, 19500],
    'Temperature_C': [80, 110, 85, 115, 75, 108, 82, 120],
    'Vibration_hz': [50, 110, 55, 130, 45, 115, 60, 140],
    'Failure': [0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

print("--- Turbine AI Training Facility Online ---")

X = df.drop("Failure",axis=1)
y = df["Failure"]

prod_pipeline = Pipeline([
    ("scaler",StandardScaler()),
    ("ai",RandomForestClassifier(random_state=42))
])

prod_pipeline.fit(X,y)

print("[SYS] Pipeline trained successfully on all data.")

joblib.dump(prod_pipeline,"turbine_engine.pkl")

print("[SYS] Engine frozen and saved to disk.")