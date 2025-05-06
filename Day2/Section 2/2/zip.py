from typing import List

def zip_example(list1: List[int], list2: List[str]):
    combined = list(zip(list1, list2))
    print(combined)

zip_example([1, 2, 3], ['a', 'b', 'c'])
