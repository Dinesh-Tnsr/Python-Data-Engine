import numpy as np
# Array 1: The current price of each stock
prices = np.array([150.0, 200.0, 50.0, 300.0, 120.0])

# Array 2: The exact number of shares you own for each stock
shares_owned = np.array([1000, 500, 2000, 100, 800])

print("Initial Prices:", prices)
print("-" * 50)

# TASK 1: The Market Crash (Scalar Vectorization)
# The market just dropped. Every single stock lost 10% of its value.

crashed_prices = prices*0.9
print("crashed prices:",crashed_prices)

# TASK 2: Total Portfolio Value (Array Vectorization)
position_values = crashed_prices*shares_owned
print("portfolio values:",position_values)

total_net_worth = sum(position_values)

print("total net worth:",total_net_worth)

