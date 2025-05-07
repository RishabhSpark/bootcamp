from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., title="User's name", example="Alice")
    age: int = Field(..., title="User's age", example=30)

print(User.schema())
