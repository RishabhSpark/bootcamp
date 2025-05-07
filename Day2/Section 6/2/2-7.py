from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)

user_dict_representation = user.dict()
print("Dictionary representation:", user_dict_representation)

user_json_representation = user.json()
print("JSON representation:", user_json_representation)
