import numpy as np
data = np.array([20,45,67,np.nan,80,43])
print("standerd mean:",np.mean(data))

missing_mask = np.isnan(data)
print("Missing mask:",missing_mask)

safe_mean = np.nanmean(data)
print("safe mean:",safe_mean)
