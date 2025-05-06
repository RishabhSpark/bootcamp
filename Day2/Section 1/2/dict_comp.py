# Dict Comprehension: Convert ["a", "b"] into {"a": 1, "b": 1}.

from typing import List, Dict

def list_to_dict(keys: List[str]) -> Dict[str, int]:
    """
    Converts a list to dictionary with each string as a key and 1 as the value
    """
    return {key: 1 for key in keys}


if __name__ == "__main__":
    values = ["a", "b"]
    ans = list_to_dict(values)
    print(ans)