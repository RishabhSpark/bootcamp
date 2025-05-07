from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

# Create two User objects
user1 = User(name="Alice", age=30)
user2 = User(name="Alice", age=30)
user3 = User(name="Bob", age=25)

# Compare users
print(user1 == user2)
print(user1 == user3)
