import pandas as pd

# Data for Stacking
roster_north = pd.DataFrame({'Emp_ID': [1, 2], 'Name': ['Amit', 'Neha']})
roster_south = pd.DataFrame({'Emp_ID': [3, 4], 'Name': ['Priya', 'Rahul']})

# Data for Reshaping (Wide Format)
wide_sales = pd.DataFrame({
    'Store': ['Delhi', 'Mumbai'],
    'Q1_Revenue': [500, 800],
    'Q2_Revenue': [600, 900]
})

print("--- Roster North ---")
print(roster_north)
print("\n--- Wide Sales Data ---")
print(wide_sales)
print("-" * 50)

master_roster =  pd.concat([roster_north,roster_south],ignore_index=True)

print(master_roster)
print("-" * 50)

long_sales = pd.melt(wide_sales,id_vars=['Store'],var_name='Quarter',value_name='Revenue')

print(long_sales)
print("-" * 50)

pivot_report = long_sales.pivot_table(index='Store',columns='Quarter',values='Revenue',aggfunc='sum')

print(pivot_report)