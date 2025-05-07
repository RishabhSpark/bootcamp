import time

start_time = time.time()

sum_result = sum(range(10000))

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
