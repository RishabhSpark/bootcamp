from pydantic import BaseModel

class User(BaseModel):
    """
    Represents a user in the system.
    
    Attributes:
        name: The name of the user.
        age: The age of the user.
        email: The email address of the user.
    """
    
    name: str
    age: int
    email: str

print(User.__doc__)
