import sys

gen = (x*x for x in range(1000000))
lst = [x*x for x in range(1000000)]

print(f"Generator memory usage: {sys.getsizeof(gen)} bytes")
print(f"List memory usage: {sys.getsizeof(lst)} bytes")
