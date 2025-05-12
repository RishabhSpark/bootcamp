from custom_types import ProcessorFn
from typing import List, Iterator, Callable

def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

def to_snakecase(text: str) -> str:
    """Convert text to snake_case."""
    return text.replace(" ", "_").lower()

def apply_processors(line: str, processors: List[ProcessorFn]) -> str:
    for processor in processors:
        line = processor(line)
    return line

def wrap_line_processor(line_fn: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    """Wrap a str -> str function to work as a stream processor."""
    def processor(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield line_fn(line)
    return processor
