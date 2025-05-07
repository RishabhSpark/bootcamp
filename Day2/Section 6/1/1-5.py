from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

    def is_adult(self) -> bool:
        return self.age>=18
    

user1 = User("Alice", 25)
print(user1.is_adult())

user2 = User("Bob", 15)
print(user2.is_adult())