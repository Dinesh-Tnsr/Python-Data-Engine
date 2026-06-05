import numpy as np

matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix_b = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

dot_product = np.dot(matrix_a,matrix_b)

clean_result = matrix_a@matrix_b

print("Dot product result using @:\n",clean_result)
print("\n")
print("using np.dot\n",dot_product)
