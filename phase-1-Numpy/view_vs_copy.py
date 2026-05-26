import numpy as np
original_data = np.array([12,13,14,15,16,17])
print("original_data:",original_data)
data_slice = original_data[0:3]

data_slice[0]=143

print("data_slice:", data_slice)
print("original_data:",original_data)
print("-"*10,"data currepted","-"*10)

print("-"*10,"The fix","-"*10)

safe_data = np.array([1,2,3,4,5,6,7,8,9])

print("safe_data:",safe_data)

my_slice = safe_data[0:3].copy()

my_slice[0]=143

print("my_slice:", my_slice)
print("safe_data:",safe_data)


