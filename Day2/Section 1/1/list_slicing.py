# List Slicing: Extract the middle 3 elements from lst = [1, 2, 3, 4, 5, 6, 7].

from typing import List, Any

def extract_middle(values: List[Any], num_elements: int):
    """
    Extracts the middle 3 elements from the list.

    Args:
        values (List[int]): The list from which to extract the middle elements.
        num_elements (int): The number of middle elements to extract.

    
    Returns:
        List[int]: The middle elements of the list.
    """

    if num_elements==0:
        return []
    
    middle_index = len(values) // 2
    start_index = middle_index - (num_elements // 2)
    
    # Adjust for odd or even number of elements
    if num_elements % 2 == 0:
        end_index = start_index + num_elements
    else:
        end_index = start_index + num_elements

    return values[start_index:end_index]

if __name__=="__main__":
    list_values = [1, 2, 3, 4, 5, 6, 7]
    ans = extract_middle(list_values, 3)
    print(ans)