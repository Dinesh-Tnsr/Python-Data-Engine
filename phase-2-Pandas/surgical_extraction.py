import numpy as np
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
print(logs_df)
print("-" * 50)

iloc_cut =  logs_df.iloc[0:3,1:3]
print(iloc_cut)

loc_cut = logs_df.loc['SRV-01':'SRV-03','CPU_Load_Pct':'RAM_Usage_GB']
print(loc_cut)

scattered_loc = logs_df.loc[['SRV-02' , 'SRV-05'],['Status' , 'Uptime_Hours']] 
print(scattered_loc)

scattered_iloc = logs_df.iloc[[1,4],[0,3]]
print(scattered_iloc)