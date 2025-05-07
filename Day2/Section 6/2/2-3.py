from pydantic import BaseModel
from typing import List

class Profile(BaseModel):
    bio: str
    skills: List[str]

class User(BaseModel):
    name: str
    age: int
    profile: Profile

user_dict = {
    "name": "Alice",
    "age": 30,
    "profile": {"bio": "Data Scientist", "skills": ["Python", "Machine Learning"]}
}

user = User(**user_dict)
print(user)
