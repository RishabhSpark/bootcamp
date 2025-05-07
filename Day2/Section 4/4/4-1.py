import itertools

id_generator = itertools.count(1)

for _ in range(10):
    print(next(id_generator))