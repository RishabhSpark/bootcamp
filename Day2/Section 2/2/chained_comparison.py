def check_range(x: int):
    if 0 < x < 10:
        print(f"{x} is between 0 and 10.")
    else:
        print(f"{x} is not between 0 and 10.")

check_range(5)
check_range(12)