import itertools

flattened = itertools.chain([1, 2], [3, 4], [5])

for item in flattened:
    print(item)
