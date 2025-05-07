from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

user1 = User(name="Alice", age=25)
user2 = User(name="Bob", age=15)

user1.tags.append("admin")
user2.tags.append("guest")

print(user1.tags)
print(user2.tags)
