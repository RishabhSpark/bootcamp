def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Returning cached result")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def slow_addition(a, b):
    print("Performing calculation...")
    return a + b

print(slow_addition(2, 3))
print(slow_addition(2, 3))