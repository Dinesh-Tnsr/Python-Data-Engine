import pandas as pd
import numpy as np

# Server 1: Corrupted CRM Orders
raw_orders = {
    'OrderID': ['ORD-101', 'ORD-102', 'ORD-103', 'ORD-104', 'ORD-105'],
    'Customer_Name': ['  Amit Sharma', 'Priya Patel  ', 'Rahul Verma', '  Neha Singh  ', 'Vikram Rao'],
    'Order_Date': ['2026-07-01', '2026-07-02', '2026-07-03', '2026-07-04', '2026-07-05'],
    'Revenue': ['$1,250.00', '$850.50', np.nan, '$2,100.75', '$500.00'],
    'Status': ['Shipped', 'Pending', 'Shipped', np.nan, 'Shipped']
}

# Server 2: Logistics Shipping Logs
raw_shipping = {
    'OrderID': ['ORD-101', 'ORD-102', 'ORD-102', 'ORD-104', 'ORD-105', 'ORD-106'],
    'Region': ['North', 'South', 'South', 'East', 'West', 'North'],
    'Shipping_Cost': [50.0, 35.0, 35.0, 80.0, 20.0, 45.0]
}

orders_df = pd.DataFrame(raw_orders,index=raw_orders['OrderID'])
shipping_df = pd.DataFrame(raw_shipping,index=raw_shipping['OrderID'])

shipping_df = shipping_df.drop_duplicates()

orders_df['Customer_Name'] = orders_df['Customer_Name'].str.strip()

orders_df[['First_name','Last_name']] = orders_df['Customer_Name'].str.split(' ',expand=True)

orders_df = orders_df.drop(columns='Customer_Name')

orders_df['Revenue'] = orders_df['Revenue'].str.replace('$', '')
orders_df['Revenue'] = orders_df['Revenue'].str.replace(',', '')
orders_df['Revenue'] = orders_df['Revenue'].astype(float)


orders_mean = orders_df['Revenue'].mean()
orders_df['Revenue'] = orders_df['Revenue'].fillna(orders_mean)

orders_df['Status'] = orders_df['Status'].fillna('Unknown')

orders_df['Order_Date'] = pd.to_datetime(orders_df['Order_Date'])

master_df = pd.merge(orders_df,shipping_df,on='OrderID',how='inner')

regional_summary = master_df.groupby('Region').agg({'Revenue' : 'sum','Shipping_Cost':'mean'})

print(regional_summary)

with pd.ExcelWriter('Executive_Dashboard.xlsx') as writer:
    master_df.to_excel(writer,sheet_name='Master_Data')
    regional_summary.to_excel(writer,sheet_name='Regional_Summary')

print(master_df)