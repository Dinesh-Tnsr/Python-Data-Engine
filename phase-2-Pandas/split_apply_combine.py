import pandas as pd

raw_data = {
    'Region': ['North', 'South', 'East', 'North', 'East', 'South', 'North'],
    'Department': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Electronics'],
    'Revenue': [50000, 30000, 45000, 25000, 35000, 40000, 55000]
}

sales_df = pd.DataFrame(raw_data)
print("--- Master Sales Ledger Online ---")
print(sales_df)
print("-" * 50)

regional_totals = sales_df.groupby('Region')['Revenue'].sum()

print(regional_totals)

dept_averages = sales_df.groupby('Department')['Revenue'].mean()

print(dept_averages)

micro_ledger = sales_df.groupby(['Region', 'Department'])['Revenue'].sum()

print(micro_ledger  )