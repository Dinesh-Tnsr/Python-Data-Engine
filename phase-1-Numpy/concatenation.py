import numpy as np

array_A = np.array([1,2,3])
array_B = np.array([4,5,6])

v_matrix = np.vstack((array_A,array_B))

print("V-stack matrix:\n",v_matrix)

extra_column = np.array([[99],
                         [99]])

h_matrix = np.hstack((v_matrix,extra_column))

print("H-stack matrix:\n",h_matrix)

