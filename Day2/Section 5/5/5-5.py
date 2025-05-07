import multiprocessing
import time

# Function to compute something in parallel
def compute_square(n):
    print(f"Square of {n} is {n * n}")
    time.sleep(1)

process = multiprocessing.Process(target=compute_square, args=(5,))
process.start()

process.join()
