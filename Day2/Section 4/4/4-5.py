import itertools

sliced = itertools.islice(range(10), 3, 7)

for item in sliced:
    print(item)
