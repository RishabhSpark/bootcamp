from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int
    email: str = Field(..., description="User's email address")

user = User(name="Alice", age=30, email="alice@example.com")
print(user)
