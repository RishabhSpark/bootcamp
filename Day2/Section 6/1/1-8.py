from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, slots=True)
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=25)

print(user1.__dict__)  # This will raise an error because __dict__ does not exist
