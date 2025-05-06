# List Operations: Append 2, remove 3, and sort the list a = [5, 3, 8].

from typing import List, Optional

def modify_list(
        values: List[int],
        to_append: Optional[int] = None,
        to_remove: Optional[int] = None,
        to_sort: bool = False
) -> List[int]:
    """
    Modifies a list by optionally appending, removing, and sorting elements.
    
    Args:
        values (List[int]): The list to modify.
        to_append (Optional[int]): Value to append, if provided.
        to_remove (Optional[int]): Value to remove, if present.
        sort (bool): Whether to sort the list after modifications.
    
    Returns:
        List[int]: The modified list.
    """
    result = values.copy()

    if to_append is not None:
        result.append(to_append)
    
    if to_remove is not None:
        result.remove(to_remove)
    
    if to_sort == True:
        result.sort()
    
    return result


if __name__ == "__main__":
    list_values = [5, 3, 8]
    ans = modify_list(
        values=list_values,
        to_append=2,
        to_remove=3,
        to_sort=True
    )
    print(ans)