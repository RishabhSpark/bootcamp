# Conditional Assignment in Comprehension: Replace negative numbers with 0 in a list using a comprehension.

from typing import List

def replace_negative_numbers(values: List[int]) -> List[int]:
    return [num if num>=0 else 0 for num in values]


if __name__ == "__main__":
    values = [-2, -1, 0, 1, 2]
    ans = replace_negative_numbers(values)
    print(ans)