from .custom_types import ProcessorFn
from typing import List

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