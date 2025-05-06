def greet_person(name: str, *, age: int) -> str:
    """
    Greets a person by name and age. The age must be provided as a keyword argument.
    
    Args:
        name (str): The name of the person.
        age (int): The age of the person. This argument is keyword-only.
    
    Returns:
        str: A greeting message including the person's name and age.
    """
    return f"Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    print(greet_person("Alice", age=30))
    # greet_person("Bob", 25)  # This would raise an error since 'age' is keyword-only
