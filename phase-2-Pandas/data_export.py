import pandas as pd

# The Master Log
raw_errors = {
    'Timestamp': ['10:00', '10:05', '10:15', '10:30'],
    'Region': ['US-East', 'EU-West', 'US-East', 'EU-West'],
    'Error_Code': [500, 404, 502, 500]
}
master_df = pd.DataFrame(raw_errors)

# The Summary Table
summary_data = {
    'Region': ['US-East', 'EU-West'],
    'Total_Errors': [2, 2],
    'Critical_Status': ['High', 'Medium']
}
summary_df = pd.DataFrame(summary_data)

print("--- DataFrames Loaded in RAM ---")
print(master_df)
print("-" * 50)

master_df.to_csv('security_log.csv',index=False)
print("Exporting security_log.csv...")

with pd.ExcelWriter('Server_Report.xlsx') as writer:
    summary_df.to_excel(writer, sheet_name='Executive_Summary', index=False)
    master_df.to_excel(writer, sheet_name='Raw_Logs', index=False)

print("Exporting Server_Report.xlsx...")