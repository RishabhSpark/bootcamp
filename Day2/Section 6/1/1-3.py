from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

user1 = User("Alice", -25)
print(user1)