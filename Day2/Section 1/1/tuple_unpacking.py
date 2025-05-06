# Tuple Unpacking: Unpack (7, 8, 9) into x, y, z and print each.

from typing import Tuple

def tuple_unpacking(values: Tuple[int, int, int]) -> None:
    """
    Unpacks a tuple into individual variables and prints them.
    
    Args:
        values (Tuple[int, int, int]): A tuple containing 3 integers to unpack.
    """
    x, y, z = values
    
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")

if __name__ == "__main__":
    values = (7, 8, 9)
    tuple_unpacking(values)