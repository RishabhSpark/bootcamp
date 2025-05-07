import itertools

original = itertools.count(1)
copy1, copy2 = itertools.tee(original, 2)

for _ in range(3):
    print(next(copy1))
for _ in range(3):
    print(next(copy2))
