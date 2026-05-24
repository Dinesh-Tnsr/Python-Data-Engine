import numpy as np
data= np.arange(1,21)
print("original data:",data)
print("-"*20)
mask1=data[(data>10) & (data%2==0)]
mask2=data[(data%3==0) | (data%7==0)]
print(mask1)
print(mask2)