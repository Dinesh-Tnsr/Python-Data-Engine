import pandas as pd

# Automatically generate 7 consecutive days starting from today
dates = pd.date_range('2026-06-25', periods=7, freq='D')

raw_data = {
    'Price': [150.0, 155.0, 152.0, 160.0, 158.0, 165.0, 170.0]
}

stock_df = pd.DataFrame(raw_data, index=dates)
print("--- Master Stock Feed Online ---")
print(stock_df)
print("-" * 50)

stock_df['Previous_Price'] = stock_df['Price'].shift(1)

print(stock_df)

stock_df['Daily_Change'] = stock_df['Price']-stock_df['Previous_Price']

print(stock_df)

stock_df['3_Day_Avg'] = stock_df['Price'].rolling(window=3).mean()

print(stock_df)

