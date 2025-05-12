def to_snakecase(text: str) -> str:
    """Convert text to snake_case."""
    return text.replace(" ", "_").lower()