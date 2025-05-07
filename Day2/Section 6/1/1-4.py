from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

user1 = User("Alice", 25)
print(user1)

try:
    user1.age = 35
except AttributeError as e:
    print(e)