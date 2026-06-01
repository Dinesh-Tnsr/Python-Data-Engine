import numpy as np
machine_data = np.array([
    [10,20,30,40],
    [11,21,31,41],
    [12,22,32,42]
])

# A 1D vector representing the baseline calibration for the 4 machines
# Shape: (4,)
calibration = np.array([100, 100, 100, 100])

# THE BROADCAST: 
# NumPy sees (3, 4) and (4,). The 4s match. 
# It instantly adds the calibration vector to EVERY row in the matrix.
calibrated_data = machine_data + calibration

print(calibrated_data)