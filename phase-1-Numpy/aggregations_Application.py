import numpy as np

# Traffic Matrix: 5 Days (Rows) x 3 Categories (Columns)
traffic_data = np.array([
    [500, 200, 800],  # Monday
    [600, 250, 750],  # Tuesday
    [550, 220, 900],  # Wednesday
    [700, 300, 950],  # Thursday
    [800, 400, 1200]  # Friday
])

print("Traffic Grid Online.")
print("-" * 50)
# TASK 1: The Global Peak
global_peak = np.max(traffic_data)
print("Global peak:",global_peak)
# TASK 2: Category Averages (Axis 0)
category_avg = np.mean(traffic_data,axis=0)
print("category averages:",category_avg)
# TASK 3: Daily Totals (Axis 1)
daily_toatl = np.sum(traffic_data,axis=1)
print("daily total:",daily_toatl)