my_list = [1, 2, 3, 4]
iterator = iter(my_list)

# Manually call next() to get the next item
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Reached the end of the iterator.")
