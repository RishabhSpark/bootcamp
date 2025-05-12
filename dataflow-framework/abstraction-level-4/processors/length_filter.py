from typing import Iterator

class LengthFilter:
    def __init__(self, min_length: int = 10):
        self.min_length = min_length

    def __call__(self, line: Iterator[str]) -> Iterator[str]:
        if len(line.strip()) >= self.min_length:
            yield line