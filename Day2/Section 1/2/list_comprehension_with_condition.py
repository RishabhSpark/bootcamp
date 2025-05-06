# List Comprehension with Condition: From [1, 2, 3, 4], make [4, 16].

from typing import List

def get_even_squares(numbers: List[int]) -> List[int]:
    """
    Returns the square of even numbers from the input list using list comprehension.
    
    Args:
        numbers (List[int]): List of integers.
    
    Returns:
        List[int]: Squares of even integers.
    """
    even_list = [n for n in numbers if n %2==0]
    return [n ** 2 for n in even_list]

if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    result = get_even_squares(input_list)
    print(result)