from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Alice", 25)
u2 = User("Alice", 25)
u3 = User("Bob", 17)

print(u1 == u2)
print(u1 == u3)