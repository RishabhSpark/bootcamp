# List vs Generator: Compare memory usage of [x for x in range(1000000)] vs (x for x in range(1000000)).

import sys
from typing import Generator, List

def compare_list_generator(n: int) -> None:
    list_comp: List[int] = [x for x in range(n)]
    gen_expr: Generator[int, None, None] = (x for x in range(n))

    print(f"List comprehension memory: {sys.getsizeof(list_comp)} bytes.")
    print(f"Generator expression memory: {sys.getsizeof(gen_expr)} bytes.")


if __name__ == "__main__":
    n = 1000000
    compare_list_generator(n)