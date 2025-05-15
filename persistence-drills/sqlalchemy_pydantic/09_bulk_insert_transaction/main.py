from sqlalchemy.orm import Session
from pydantic import ValidationError
from models import User, UserSchema, SessionLocal, EmailUpdateSchema, UserWithPostsSchema, Post
from typing import Optional, List, Dict
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import delete
import json


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

def insert_multiple_users(users_data: List[Dict[str, str]], db: Session) -> None:
    try:
        with db.begin():  # begin a transaction block
            for user_data in users_data:
                # Validate each user data using Pydantic
                user_schema = UserSchema(**user_data)
                
                new_user = User(name=user_schema.name, email=user_schema.email)
                db.add(new_user)

        print(f"Inserted {len(users_data)} users successfully.")
    except ValidationError as ve:
        db.rollback()
        print(f"Validation error: {ve}")
    except SQLAlchemyError as sae:
        db.rollback()
        print(f"Database error during bulk insert: {sae}")
    except Exception as e:
        db.rollback()
        print(f"Unexpected error during bulk insert: {e}")

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

def update_user_email(user_id: int, new_email: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            print(f"No user found with id {user_id}")
            return

        validated_email = EmailUpdateSchema(email=new_email).email

        user.email = validated_email
        session.commit()
        print(f"User email updated successfully to {user.email}")

    except ValidationError as ve:
        print("Invalid email format:", ve)
        session.rollback()
    except SQLAlchemyError as e:
        print("Database error:", e)
        session.rollback()
    finally:
        session.close()

def delete_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"No user found with ID {user_id}")
            return

        stmt = delete(User).where(User.id == user_id)
        session.execute(stmt)
        session.commit()
        print(f"User with ID {user_id} has been deleted.")

    except SQLAlchemyError as e:
        print("Error occurred while deleting user:", e)
        session.rollback()
    finally:
        session.close()
 
def insert_post_for_user(user_id: int, title: str, content: str):
    db = SessionLocal()
    try:
        new_post = Post(title=title, content=content, user_id=user_id)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        print(f"Inserted post: '{new_post.title}' for user ID {user_id}")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Database error: {e}")
    finally:
        db.close()
        
def get_user_with_posts(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user_data = UserWithPostsSchema.model_validate(user)
            print(json.dumps(user_data.model_dump(), indent=2))
        else:
            print(f"No user found with ID {user_id}")
    except Exception as e:
        print(f"Error fetching user with posts: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    users_to_insert = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    db = SessionLocal()
    insert_multiple_users(users_to_insert, db)
    db.close()