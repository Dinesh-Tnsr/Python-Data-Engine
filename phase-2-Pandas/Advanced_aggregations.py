import pandas as pd

raw_data = {
    'Transaction_ID': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6'],
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
    'Department': ['Tech', 'Gear', 'Gear', 'Tech', 'Tech', 'Gear'],
    'Revenue': [1200, 800, 400, 3000, 1500, 600],
    'Units_Sold': [4, 2, 8, 10, 5, 3]
}

sales_df = pd.DataFrame(raw_data)
print("--- Master Ledger Online ---")
print(sales_df)
print("-" * 50)

multi_stat_df = sales_df.groupby('Region')['Revenue'].agg(['sum','mean','max'])

print(multi_stat_df)

logistics_df = sales_df.groupby('Department').agg({'Revenue':'sum','Units_Sold':'max'})

print(logistics_df)

sales_df['Regional_Total'] = sales_df.groupby('Region')['Revenue'].transform('sum')

print(sales_df)

sales_df['Pct_Of_Region'] = sales_df['Revenue']/sales_df['Regional_Total']

print(sales_df)