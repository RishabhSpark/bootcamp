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

if __name__ == "__main__":
    user_data = {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    # Create a new session and insert the user
    with SessionLocal() as db:
        insert_user(user_data, db)
