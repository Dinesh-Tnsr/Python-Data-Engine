import pandas as pd

# The Left Table (HR System)
users_data = {
    'User_ID': ['U1', 'U2', 'U3', 'U4'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Engineering', 'Engineering', 'Marketing']
}
users_df = pd.DataFrame(users_data)

# The Right Table (IT System)
hardware_data = {
    'User_ID': ['U2', 'U3', 'U5'],
    'Device': ['MacBook Pro', 'ThinkPad', 'Dell XPS'],
    'Asset_Tag': ['MAC-01', 'THK-99', 'DEL-42']
}
hardware_df = pd.DataFrame(hardware_data)

print("--- HR Users Table (Left) ---")
print(users_df)
print("\n--- IT Hardware Table (Right) ---")
print(hardware_df)
print("-" * 50)

equipped_users = pd.merge(users_df,hardware_df,on='User_ID',how='inner')

print(equipped_users)

print("-" * 50)

all_users = pd.merge(users_df,hardware_df,on='User_ID',how='left')

print(all_users)

print("-" * 50)

master_audit = pd.merge(users_df,hardware_df,on='User_ID',how='outer')

print(master_audit)

print("total holes:\n",master_audit.isna().sum())