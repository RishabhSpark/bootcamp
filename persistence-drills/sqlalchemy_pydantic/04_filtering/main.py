from sqlalchemy.orm import Session
from pydantic import ValidationError
from models import User, UserSchema, SessionLocal
from typing import Optional
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def insert_user(user_data: dict, db: Session):
    try:
        user_schema = UserSchema(**user_data)
        
        new_user = User(name=user_schema.name, email=user_schema.email)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        print(f"Inserted new user: {new_user.name} with email: {new_user.email}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"An error occurred while inserting the user: {e}")

# Fetch all users from the database and convert them to Pydantic models
def fetch_users(db: Session):
    try:
        users = db.query(User).all()
        
        user_schemas = [UserSchema.model_validate(user) for user in users]
        
        return user_schemas
    except Exception as e:
        print(f"An error occurred while fetching users: {e}")
        return []

# Display users in a structured format
def display_users(users):
    if users:
        print("Users in the database:")
        for user in users:
            print(f"Name: {user.name}, Email: {user.email}")
    else:
        print("No users found.")

def get_user_by_email(email: str, db: Session) -> Optional[UserSchema]:
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            return UserSchema.model_validate(user)
        else:
            return None
    except Exception as e:
        print(f"Error fetching user by email: {e}")
        return None

if __name__ == "__main__":
    # Create a new session and insert the user
    with SessionLocal() as db:
        email_to_search = "alice.johnson@example.com"

        with SessionLocal() as db:
            user_schema = get_user_by_email(email_to_search, db)

            if user_schema:
                print(f"User found: Name = {user_schema.name}, Email = {user_schema.email}")
            else:
                print(f"No user found with email: {email_to_search}")
