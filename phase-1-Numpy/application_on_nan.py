import numpy as np
voltages = np.array([240.0, 238.5, np.nan, 242.1, 239.0, np.nan, 241.5])
print("raw voltages:",voltages)
print("-"*40)

safe_avg_voltage=np.nanmean(voltages)
print("safe average voltages:",safe_avg_voltage)

safe_voltages = np.where(np.isnan(voltages), safe_avg_voltage, voltages)
print("Repaired voltages:", safe_voltages)

