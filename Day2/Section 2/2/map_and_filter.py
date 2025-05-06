from typing import List

def double_numbers(lst: List[int]):
    doubled = list(map(lambda x: x * 2, lst))
    print(doubled)

def remove_even_numbers(lst: List[int]):
    filtered = list(filter(lambda x: x % 2 != 0, lst))
    print(filtered)

lst = [1, 2, 3, 4]
double_numbers(lst)
remove_even_numbers(lst)