def info(name: str, age: int = 0) -> str:
    """
    Returns a string containing the user's name and age.
    """
    return f"{name} is {age} years old."

if __name__ == "__main__":
    print(info(name="Alice", age=30))
    print(info(age=25, name="Bob"))
    print(info("Charlie"))