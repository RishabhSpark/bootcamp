# Default Arguments: Create greet(name="Guest") and test with and without passing a name.

def greet(name: str = "Guest") -> str:
    """
    Greets the user by name, defaulting to 'Guest' if no name is provided.
    """

    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet())
    print(greet("Rishabh"))