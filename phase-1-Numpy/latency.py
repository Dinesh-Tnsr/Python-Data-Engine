import time

start_time = time.time()

for i in range(1000000):
    pass

end_time = time.time()

latency =  end_time-start_time

print(f"Execution time:{latency}seconds")
