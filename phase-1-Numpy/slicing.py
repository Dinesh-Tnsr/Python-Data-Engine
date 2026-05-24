import numpy as np
matrix=np.arange(1,26).reshape(5,5)
print("original matrix")
print(matrix)
print('-'*20)
slice1=matrix[1:4,1:4]
slice2=matrix[0:5,4:5]
print(slice1)
print(slice2)
