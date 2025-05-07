from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

user_dict = {"name": "Bob", "age": "not a number"}

try:
    user = User(**user_dict)
except ValidationError as e:
    print(f"Validation Error: {e}")