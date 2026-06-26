import pandas as pd

raw_data = {
    'Customer_ID': ['C-01', 'C-02', 'C-03'],
    'Raw_Name': ['  Amit Kumar          ', 'Priya Sharma', 'Rahul Singh  '],
    'Email': ['amit@gmail.com', 'priya@yahoo.com', 'rahul@gmail.com'],
    'Revenue': ['$1,500.50', '$2,400.00', '$850.75']
}

crm_df = pd.DataFrame(raw_data)
print("--- Messy CRM Data Online ---")
print(crm_df)
print("-" * 50)

crm_df['Raw_Name'] = crm_df['Raw_Name'].str.strip()

print(crm_df)
print("-" * 50)

crm_df['Revenue'] = crm_df['Revenue'].str.replace('$','')
crm_df['Revenue'] = crm_df['Revenue'].str.replace(',','')

print(crm_df)
print("-" * 50)

crm_df['Revenue'] = crm_df['Revenue'].astype(float)
print(crm_df)
print("-" * 50)

crm_df[['First_Name', 'Last_Name']] = crm_df['Raw_Name'].str.split(' ',expand=True)
print(crm_df)
print("-" * 50)

crm_df = crm_df.drop(columns=['Raw_Name'])
print(crm_df)

mask = crm_df['Email'].str.contains('gmail.com')

gmail_users = crm_df[mask]

print(gmail_users)