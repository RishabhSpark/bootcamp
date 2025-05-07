from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

user1 = User("Alice", 25)
print(user1)