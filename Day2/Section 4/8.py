def make_closure_add(value):
    return lambda x: x + value

add_five = make_closure_add(5)
print(add_five(10))