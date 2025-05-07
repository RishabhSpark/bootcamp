import time

def fib_uncached(n):
    if n <= 1:
        return n
    return fib_uncached(n-1) + fib_uncached(n-2)

start_time = time.time()
print(fib_uncached(30))
end_time = time.time()
print(f"Uncached Fibonacci execution time: {end_time - start_time} seconds")
