import itertools

def count_up_to(max_value):
    count = 0
    while count < max_value:
        yield count
        count += 1

first_10 = itertools.islice(count_up_to(100), 10)
for num in first_10:
    print(num)
