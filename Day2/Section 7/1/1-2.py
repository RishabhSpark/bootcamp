import timeit

list_time = timeit.timeit("[x*x for x in range(1000000)]", number=10)

generator_time = timeit.timeit("(x*x for x in range(1000000))", number=10)

print(f"List comprehension time: {list_time} seconds")
print(f"Generator expression time: {generator_time} seconds")
