def swap_values(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")

swap_values(5, 10)