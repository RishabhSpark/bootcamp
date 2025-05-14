# main.py
from sqlalchemy.orm import Session
from pydantic import ValidationError
from models import User, UserSchema, SessionLocal

# Create a SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Insert a new user after validating data with Pydantic
def insert_user(user_data: dict, db: Session):
    try:
        user_schema = UserSchema(**user_data)
        
        # Create a new SQLAlchemy User instance
        new_user = User(name=user_schema.name, email=user_schema.email)
        
        # Add the new user to the session and commit
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Refresh to get the updated data from the database
        
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

if __name__ == "__main__":
    user_data = {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    # Create a new session and insert the user
    with SessionLocal() as db:
        insert_user(user_data, db)

        users = fetch_users(db)
        display_users(users)