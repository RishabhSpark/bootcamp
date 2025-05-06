from typing import List

def sort_by_second_item(lst: List[int]):
    sorted_lst = sorted(lst, key=lambda x: x[1])
    print(sorted_lst)

sort_by_second_item([(1, 3), (2, 1), (3, 2)])
