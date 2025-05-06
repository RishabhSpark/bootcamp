from typing import Dict

def iterate_dict(person: Dict[str, int]) -> None:
    """
    Iterates over a dictionary and prints its keys and values.
    
    Args:
        person (Dict[str, int]): A dictionary containing keys and values to iterate over.
    """
    for key, value in person.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    person = {"name": "Bob", "age": 30}
    iterate_dict(person)