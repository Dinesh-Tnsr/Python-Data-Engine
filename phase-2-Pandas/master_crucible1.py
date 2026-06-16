import numpy as np
import pandas as pd

df = pd.read_csv('corrupted_telemetry.csv')
print("-"*20, "CSV file readed.", "-"*20)

print(df)

df = df.drop_duplicates()
print("-"*20, "Duplicates removed.", "-"*20)

print(df)

df['Sensor_Type'] = df['Sensor_Type'].fillna('Unknown')
print("-"*20, "Sensor_Type filled with Unknown.", "-"*20)

print(df)

mean_signal_strength = df['Signal_Strength'].mean()
print("-"*20, "Mean signal strength calculated.", "-"*20)

print(mean_signal_strength)

df['Signal_Strength'] = df['Signal_Strength'].fillna(mean_signal_strength)
print("-"*20, "Signal_Strength filled with mean value.", "-"*20)

print(df)

df['Packet_ID'] = df['Packet_ID'].astype(str)
print("-"*20, "Packet_ID converted to string.", "-"*20)

print(df)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
print("-"*20, "Timestamp converted to datetime.", "-"*20)

print(df)

print(df.info())