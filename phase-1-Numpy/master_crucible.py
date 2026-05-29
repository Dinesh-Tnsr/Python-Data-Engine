import numpy as np
np.random.seed(999)
# Creating the 3D Tensor (5x5 grid, 3 sensor channels)
drone_scan = np.random.randint(10,200,size=(5,5,3)).astype(float)
# Injecting the magnetic corruption into the Temperature channel (Channel 0)

drone_scan[1,1,0] = np.nan
drone_scan[3,4,0] = np.nan
drone_scan[0,2,0] = 500.0  # Impossible spike

print("system initialized. Tensor shape :\n",drone_scan.shape)

mask = np.isnan(drone_scan)
# TASK 1: Safe Extraction (3D Slicing + Memory Pointer Management)
temp_map = drone_scan[:,:,0].copy()
print("temperature channnel:\n",temp_map)
# TASK 2: The Baseline (Handling the Void)
safe_avg_temp = np.nanmean(temp_map)
print("safe average temperature:\n",safe_avg_temp)
# TASK 3: The Repair (Mutation + NaN Detection)
repaired_temp = np.where(mask[:,:,0],safe_avg_temp,temp_map)
print("repaired temperature channel:\n",repaired_temp)
# TASK 4: The Safety Cap (Advanced Mutation)
temp_map = np.where(repaired_temp>150,150,repaired_temp)
print("updated temperature channel:\n",temp_map)
# TASK 5: The Final Target (2D Slicing)
dashboard_view = temp_map[1:4,1:4]
print("Center grid(dashboard view):\n",dashboard_view)