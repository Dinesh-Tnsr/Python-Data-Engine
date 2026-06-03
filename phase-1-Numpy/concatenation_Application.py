import numpy as np
# Morning Shift: 3 machines, 2 readings each (Shape: 2, 3)
morning_shift = np.array([
    [10.1,12.2,11.5],
    [10.5,12.4,11.8]
])

# Evening Shift: 3 machines, 2 readings each (Shape: 2, 3)

evening_shift = np.array([
    [11.0, 12.1, 11.4],
    [11.2, 12.6, 11.9]
])

# Supervisor IDs: 4 readings total, 1 column (Shape: 4, 1)
# Supervisor 99 ran the morning, Supervisor 88 ran the evening.
supervisor_ids = np.array([
    [99],
    [99],
    [88],
    [88]
])

print("Data Systems Online.")
print("-" * 50)
# TASK 1: The Timeline Merge
full_day = np.vstack((morning_shift,evening_shift))
# TASK 2: The Metadata Attach
final_report = np.hstack((full_day,supervisor_ids))
# TASK 3: Verification
print("final_report:\n",final_report)