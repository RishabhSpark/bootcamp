# Set Comprehension: From "hello world", get all unique vowels.
from typing import Set

def unique_vowels_from_string(string: str) -> Set[str]:
    """
    Extract all vowels from string
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}

    unique_vowels = set()
    for char in string:
        if char in vowels:
            unique_vowels.add(char)

    return unique_vowels


if __name__=="__main__":
    text = "Hello World"
    ans = unique_vowels_from_string(text)
    print(ans)    