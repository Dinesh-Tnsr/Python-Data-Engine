import numpy as np
np.random.seed(42)
raw_temps = np.random.randint(0,120,size=15)
machines = np.random.randint(0,6,size=15)
print("Raw temperatures:",raw_temps)
print("Machine ID's:",machines)
print("-"*40)

safe_temps= np.where( raw_temps<10, 10, raw_temps )

target_machines=[2,4]
mask=np.isin( machines, target_machines )
audited_machines = machines[mask]

print("safe temperatures:",safe_temps)

print("Audited machines:",audited_machines)