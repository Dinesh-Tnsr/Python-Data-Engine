import numpy as np

sales_matrix = np.array([
    [10, 20, 30, 40], # Day 1
    [10, 10, 10, 10], # Day 2
    [5,   5,  5,  5]  # Day 3
])

# 1. Total Annihilation (No Axis)
total_sum = np.sum(sales_matrix)
print("Total sales:",total_sum)
# 2. Axis 0: The Vertical Crush (Per Product)
product_total= np.sum(sales_matrix,axis=0)
print("per product sales:",product_total)
# 3. Axis 1: The Horizontal Crush (Per Day)
daily_total = np.sum(sales_matrix,axis=1)
print("per day sales:",daily_total)

