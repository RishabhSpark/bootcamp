from pydantic import BaseModel, conint, constr, ValidationError

class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)  # Age must be greater than 0

user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)
print(user)

try:
    user_dict = {"name": "Al", "age": -1}
    user = User(**user_dict)
except ValidationError as e:
    print(f"Validation Error: {e}")
