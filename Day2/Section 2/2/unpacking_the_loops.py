from typing import List

def unpack_in_loops(lst: List[int]):
    for x, y in lst:
        print(f"x: {x}, y: {y}")

unpack_in_loops([(1, 2), (3, 4), (5, 6)])
