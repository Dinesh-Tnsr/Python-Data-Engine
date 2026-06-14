import pandas as pd
import numpy as np

raw_data = {
    'Sensor_ID': ['S-1', 'S-2', 'S-3', 'S-4', 'S-5'],
    'Location': ['Zone A', 'Zone B', np.nan, 'Zone C', 'Zone A'],
    'Temp_C': [45.2, np.nan, 47.1, 46.5, np.nan],
    'Status': ['Active', 'Active', 'Maintenance', 'Active', 'Active']
}

sensor_df = pd.DataFrame(raw_data)
print("--- Corrupted DataFrame Online ---")
print(sensor_df)
print("-" * 50)

missing_values = sensor_df.isna().sum()

print(missing_values)

strict_df = sensor_df.dropna()

print(strict_df)

sensor_df['Location'] = sensor_df['Location'].fillna('Unknown')

print(sensor_df['Location'])

mean_temp = sensor_df['Temp_C'].mean()

sensor_df['Temp_C'] = sensor_df['Temp_C'].fillna(mean_temp)

print(sensor_df['Temp_C'])

check = sensor_df.isna().sum()

print(check)

print("\n--- Fully Repaired DataFrame ---")
print(sensor_df)