import pandas as pd
from sklearn.linear_model import LinearRegression

# Synthetic Housing Data
# Bedrooms, Bathrooms, Age_of_House, Price
data = {
    'Bedrooms': [2, 3, 4, 3, 5],
    'Bathrooms': [1, 2, 3, 2, 4],
    'Age': [10, 5, 2, 15, 1],
    'Price': [250000, 350000, 500000, 300000, 650000]
}

df = pd.DataFrame(data)
print("--- Scikit-Learn Engine Online ---")

y = df["Price"]
X = df.drop("Price",axis=1)

model = LinearRegression()
model.fit(X,y)
new_house = pd.DataFrame({"Bedrooms":[3],"Bathrooms":[2],"Age":[10]})

predicted_price = model.predict(new_house)

print(predicted_price)