from typing import List, Any

def enumerate_example(lst: List[Any]):
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")

enumerate_example([10, 20, 30, 40])