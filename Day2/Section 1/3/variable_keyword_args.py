from typing import Dict

def show_settings(**kwargs: Dict[str, str]) -> None:
    """
    Prints all key-value pairs from the keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    show_settings(theme="dark", font="Arial", size="12")  