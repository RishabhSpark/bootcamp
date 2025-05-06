from contextlib import suppress

my_dict = {"name": "Alice"}

with suppress(KeyError):
    print(my_dict["age"])