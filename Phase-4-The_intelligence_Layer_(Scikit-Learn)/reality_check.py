import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    'Bedrooms': [2, 3, 4, 3, 5, 2, 4, 3, 5, 4],
    'Bathrooms': [1, 2, 3, 2, 4, 1, 3, 2, 4, 3],
    'Age': [10, 5, 2, 15, 1, 12, 4, 8, 2, 6],
    'Price': [250000, 350000, 500000, 300000, 650000, 240000, 480000, 330000, 640000, 470000]
}

df = pd.DataFrame(data)
print("--- Reality Check Engine Online ---")

y = df["Price"]
X = df.drop("Price",axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

print(predictions)
print("-"*100)
print(y_test)