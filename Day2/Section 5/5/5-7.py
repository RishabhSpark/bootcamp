import concurrent.futures

def compute_square(n):
    return n * n

# Use ThreadPoolExecutor to parallelize function calls
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(compute_square, [1, 2, 3, 4, 5])
    for result in results:
        print(result)
