def unpack_list() -> None:
    a, b, *rest = [1, 2, 3, 4, 5]
    print(f"a: {a}, b: {b}, rest: {rest}")

unpack_list()