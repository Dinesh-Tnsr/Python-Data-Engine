import numpy as np
base_array = np.array([10,20,30,40])

boosted_array = base_array + 5
print("Boosted:",boosted_array)

weights = np.array([2,2,3,3])
final_array = base_array*weights
print("Final array:",final_array)