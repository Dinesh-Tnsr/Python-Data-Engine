import numpy as np
import pandas as pd

print("Booting Ingestion Engine...")
print("-" * 50)

logs_df = pd.read_csv('server_logs.csv')
print(logs_df)

print("-"*20,"server preview","-"*20)

print(logs_df.head(3))

print("-"*20,"scheema Audit","-"*20)

print(logs_df.info())

print("-"*20,"Statistical Summary","-"*20)

print(logs_df.describe())