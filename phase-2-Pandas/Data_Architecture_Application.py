import numpy as np
import pandas as pd

prices = pd.Series(
    data = [199.99, 45.50, 899.00],
    index = ["SKU-100", "SKU-101", "SKU-102"]
)

print(prices)

raw_data = {
    "Product_Name": ["Headphones", "Mouse", "Monitor"],
    "Stock_Count" : [50, 120, 15]
}

inventary_df = pd.DataFrame( raw_data,index=["SKU-100", "SKU-101", "SKU-102"])

print(inventary_df)

inventary_df["Price"] = prices

print("\n--- Final Master Inventory ---")
print(inventary_df)