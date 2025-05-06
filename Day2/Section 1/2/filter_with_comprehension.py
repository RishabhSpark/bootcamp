# Filter with Comprehension: Extract even-length strings from ["hi", "hello", "bye"].

from typing import List

def filter_even_length_words(words: List[str]) -> List[str]:
    return [word for word in words if len(word) % 2 == 0]

if __name__ == "__main__":
    input_words = ["hi", "hello", "bye"]
    ans = filter_even_length_words(input_words)
    print(ans)
