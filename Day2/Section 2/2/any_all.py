from typing import List

def check_numbers(lst: List[int]):
    if any(x < 0 for x in lst):
        print("There is at least one negative number.")
    else:
        print("No negative numbers.")
    
    if all(x > 0 for x in lst):
        print("All numbers are positive.")
    else:
        print("Not all numbers are positive.")

check_numbers([1, -2, 3, 4])
