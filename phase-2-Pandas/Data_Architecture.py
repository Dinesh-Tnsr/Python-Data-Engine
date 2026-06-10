import pandas as pd

sales_data = pd.Series(
    data=[500, 800, 1200], 
    index=["Monday", "Tuesday", "Wednesday"],
    name="Daily_Revenue"
)
print("--- 1D Series ---")
print(sales_data)

raw_data = {
    "Employee": ["Rahul", "Priya", "Amit"],
    "Department": ["IT", "HR", "Finance"],
    "Salary": [85000, 72000, 95000]
}

df = pd.DataFrame(raw_data, index=["EMP-01", "EMP-02", "EMP-03"])
print("\n--- 2D DataFrame ---")
print(df)