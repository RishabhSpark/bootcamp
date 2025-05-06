class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def set_age(age: int):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age

try:
    age = set_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")