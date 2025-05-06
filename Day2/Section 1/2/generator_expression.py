# Generator Expression: Use (n*n for n in range(5)) to build a generator and print its items.

from typing import Generator

def square_generator(limit: int) -> Generator[int, None, None]:
    """
    Generates squares of numbers from 0 to limit - 1 using a generator expression.
    """
    return (n * n for n in range(limit))

if __name__ == "__main__":
    gen = square_generator(5)
    for val in gen:
        print(val)