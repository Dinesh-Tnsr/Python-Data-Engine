import pandas as pd

raw_data = {
    'Server_ID': ['SRV-01', 'SRV-02', 'SRV-03', 'SRV-04', 'SRV-05'],
    'Status': ['Active', 'Active', 'Offline', 'Active', 'Maintenance'],
    'CPU_Load_Pct': [45.2, 89.5, 0.0, 72.1, 10.0],
    'RAM_Usage_GB': [16.5, 31.0, 0.0, 24.5, 4.2],
    'Uptime_Hours': [120, 2040, 0, 85, 12]
}

logs_df = pd.DataFrame(raw_data)
logs_df.set_index('Server_ID', inplace=True)
print("--- Master DataFrame Online ---")

mask = logs_df['CPU_Load_Pct']>70
heavy_load_df = logs_df[mask]

print(heavy_load_df)

mask1 = ((logs_df['CPU_Load_Pct']>80) & (logs_df['Status']=='Active'))
critical_df = logs_df[mask1]

print(critical_df)

mask2 = logs_df['Status'].isin(['Offline','Maintenance'])
patch_list_df = logs_df[mask2]

print(patch_list_df)

mask3 = logs_df['Status'].str.contains('ive')
cut_list_df = logs_df[mask3]

print(cut_list_df)