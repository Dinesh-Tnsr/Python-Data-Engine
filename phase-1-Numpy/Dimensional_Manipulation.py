import numpy as np

raw_data = np.array([1,2,3,4,5,6,7,8,9,10])

matrix_2D = raw_data.reshape(2,5)

print("reshaped 2D matrix:\n",matrix_2D)

flipped_matrix = matrix_2D.T

print("Transpose of matrix_2D:\n",flipped_matrix)

crushed_matrix1 = flipped_matrix.flatten()

crushed_matrix2 = matrix_2D.flatten()

print("Flattened matrix:\n",crushed_matrix1)
print("Flattened matrix:\n",crushed_matrix2)