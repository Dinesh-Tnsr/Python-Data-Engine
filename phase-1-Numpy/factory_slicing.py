import numpy as np
np.random.seed(99)
factory_data = np.random.randint(10,100,size=(15,3))
print("raw factory data (15 rows and 3 coloums:")
print(factory_data)
print("-"*20)

vibrational_data = factory_data[0:15,1:2]
print("Vibrationnal Data:")
print(vibrational_data)

danger_rows_T= factory_data[:,0]
danger_rows_P= factory_data[:,2]

danger_mask= (danger_rows_T > 80) | (danger_rows_P < 20)

danger_rows = factory_data[danger_mask]
print(danger_rows)