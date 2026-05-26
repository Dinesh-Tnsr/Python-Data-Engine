import numpy as np

master_record = np.array([105,110,95,115,120])
print("master record:",master_record)

sim_data = master_record[2:,].copy()


sim_data = sim_data + 50

print("sim_data:",sim_data)
print("master_record:",master_record)
