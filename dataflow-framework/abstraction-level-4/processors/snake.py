import re

def to_snakecase(text: str) -> str:
    """Convert text to snake_case."""
    words = re.findall(r'\b\w+\b', text.strip())
    return '_'.join(words).lower()