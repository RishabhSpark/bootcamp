# Nested List Comprehension: Flatten [[1,2],[3,4]] into [1,2,3,4].

from typing import List

def flatten_list(values: List[List[int]]) -> List[int]:
    """
    Flattens a 2D list into a 1D list using nested list comprehension.
    
    Args:
        nested_list (List[List[int]]): A 2D list of integers.
    
    Returns:
        List[int]: A flattened 1D list.
    """
    ans = []
    for sublist in values:
        for items in sublist:
            ans.append(items)

    return ans

if __name__ == "__main__":
    values = [[1, 2], [3, 4]]
    ans = flatten_list(values)
    print(ans)