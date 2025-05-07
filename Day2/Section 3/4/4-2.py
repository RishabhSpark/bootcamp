from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

u1 = User("Bob")
u2 = User("Alice", 25)
print(u1)
print(u2)