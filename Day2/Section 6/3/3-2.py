from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")
    name: str
    age: int

json_input = {"user_id": 1, "name": "Alice", "age": 30}

user = User.parse_obj(json_input)
print(user)
