import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Massive scale imbalance between features
data = {
    'Bedrooms': [2, 3, 4, 3, 5, 2, 4, 3, 5, 4],
    'Sq_Ft': [800, 1500, 2500, 1400, 3500, 900, 2400, 1600, 3600, 2200],
    'Price': [250000, 350000, 500000, 300000, 650000, 240000, 480000, 330000, 640000, 470000] 
    
}
df = pd.DataFrame(data)
print("--- Mathematical Scaling Engine Online ---")

y = df["Price"]
X = df.drop("Price", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print(X_train_scaled)
print("-"*100)
print(X_test_scaled)
