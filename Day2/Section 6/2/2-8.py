from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    country: Optional[str] = None

user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)

print(user)
