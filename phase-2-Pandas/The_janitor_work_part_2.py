import pandas as pd

raw_data = {
    'Transaction_ID': ['TX-01', 'TX-02', 'TX-02', 'TX-03', 'TX-04'],
    'Date': ['2026-06-15', '2026-06-15', '2026-06-15', '2026-06-16', '2026-06-16'],
    'Customer': ['Amit', 'Priya', 'Priya', 'Rahul', 'Neha'],
    'Revenue': ['1500.50', '2400.00', '2400.00', '850.75', '3200.00'] # String!
}

sales_df = pd.DataFrame(raw_data)
print("--- Corrupted Data Online ---")
print(sales_df)
print("\n--- Schema Before ---")
print(sales_df.info())
print("-" * 50)

clean_df = sales_df.drop_duplicates()
print("-"*20,"duplicate rows dropped","-"*20)
print(clean_df)

clean_df['Revenue'] = clean_df['Revenue'].astype(float)
print("-"*10,"conversion from string to float of revenue coloum","-"*10)
print(clean_df)

clean_df['Date'] = pd.to_datetime(clean_df['Date'])
print("-"*10,"conversion from string to float of Date coloum","-"*10)
print(clean_df)

print(clean_df.info())



