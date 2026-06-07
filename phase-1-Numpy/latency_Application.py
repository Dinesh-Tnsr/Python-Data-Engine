import numpy as np
import time
import random

print("Allocating 1 crore data points in RAM... Please wait.")

python_list = [random.randint(1,100) for _ in range(10000000)]

numpy_array = np.array(python_list)

print("Data Structures Online. Ready for the race.")
print("-"*50)

start_time = time.time()

operation1 = [x*x for x in python_list]


end_time = time.time()
operation1_time = end_time-start_time
print("Execution time (1):",operation1_time)

start_time = time.time()

operation2 = numpy_array**2

end_time = time.time()

operation2_time = end_time-start_time

print("Execution time (2):",operation2_time)

time_diff_ratio = operation1_time/operation2_time

print("Numpy is",time_diff_ratio,"times faster than standard python")



