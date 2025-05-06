from typing import Tuple, Dict

def display_info(*args: Tuple[str, ...], **kwargs: Dict[str, str]) -> None:
    """
    Displays information by accepting both positional and keyword arguments.
    
    Args:
        *args: A variable number of positional arguments.
        **kwargs: A variable number of keyword arguments.
    """
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    display_info("Alice", "Bob", name="Alice", age="30")