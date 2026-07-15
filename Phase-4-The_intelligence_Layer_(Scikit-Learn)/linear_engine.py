import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Synthetic California Housing Data (15 rows)
np.random.seed(42)
data = {
    'Bedrooms': np.random.randint(2, 6, 15),
    'Bathrooms': np.random.randint(1, 4, 15),
    'Sq_Ft': np.random.randint(1000, 4000, 15),
    'Age': np.random.randint(1, 50, 15),
    # Price is roughly derived from the features with some random noise added
}
df = pd.DataFrame(data)
df['Price'] = (df['Bedrooms']*50000) + (df['Bathrooms']*25000) + (df['Sq_Ft']*150) - (df['Age']*2000) + np.random.randint(-20000, 20000, 15)

print("--- Continuous Prediction Engine Online ---")

y = df["Price"]
X = df.drop("Price", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
X_train_data = scaler.fit_transform(X_train)
X_test_data = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_data,y_train)

predictions = model.predict(X_test_data)

print(predictions)
print("-"*100)
print(mean_absolute_error(y_test,predictions))
print("-"*100)
print(np.sqrt(mean_squared_error(y_test,predictions)))
print("-"*100)
print(r2_score(y_test,predictions))