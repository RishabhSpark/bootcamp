from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)

print(user)
