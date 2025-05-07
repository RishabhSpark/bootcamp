from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Zhongli", 40)
print(u)