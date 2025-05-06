from typing import Tuple

def add_all(*args: Tuple[int, ...]) -> int:
    """
    Returns the sum of all the arguments passed to the function.
    """
    return sum(args)

if __name__ == "__main__":
    print(add_all(1, 2, 3))
    print(add_all(10, 20, 30, 40))
    print(add_all(5))
