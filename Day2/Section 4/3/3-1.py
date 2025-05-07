from functools import partial

int_base2 = partial(int, base=2)

print(int_base2("1010"))