import asyncio
from typing import List, Dict, Optional
from pydantic import ValidationError
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from models import User, UserSchema, AsyncSessionLocal, EmailUpdateSchema, UserWithPostsSchema, Post
import json


async def insert_user(user_data: dict):
    async with AsyncSessionLocal() as session:
        try:
            user_schema = UserSchema(**user_data)
            new_user = User(name=user_schema.name, email=user_schema.email)
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            print(f"Inserted new user: {new_user.name} with email: {new_user.email}")
        except ValidationError as e:
            print(f"Validation error: {e}")
        except Exception as e:
            print(f"An error occurred while inserting the user: {e}")

async def insert_multiple_users(users_data: List[Dict[str, str]]):
    async with AsyncSessionLocal() as session:
        try:
            async with session.begin():
                for user_data in users_data:
                    user_schema = UserSchema(**user_data)
                    session.add(User(name=user_schema.name, email=user_schema.email))
            print(f"Inserted {len(users_data)} users successfully.")
        except Exception as e:
            print(f"Error inserting users: {e}")

async def fetch_users():
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(select(User))
            users = result.scalars().all()
            return [UserSchema.model_validate(user) for user in users]
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

def display_users(users: List[UserSchema]):
    if users:
        print("Users in the database:")
        for user in users:
            print(f"Name: {user.name}, Email: {user.email}")
    else:
        print("No users found.")

async def get_user_by_email(email: str) -> Optional[UserSchema]:
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(select(User).where(User.email == email))
            user = result.scalars().first()
            return UserSchema.model_validate(user) if user else None
        except Exception as e:
            print(f"Error fetching user by email: {e}")
            return None

async def update_user_email(user_id: int, new_email: str):
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(select(User).where(User.id == user_id))
            user = result.scalars().first()
            if not user:
                print(f"No user found with ID {user_id}")
                return
            validated_email = EmailUpdateSchema(email=new_email).email
            user.email = validated_email
            await session.commit()
            print(f"User email updated successfully to {user.email}")
        except Exception as e:
            await session.rollback()
            print(f"Error updating user email: {e}")

async def delete_user(user_id: int):
    async with AsyncSessionLocal() as session:
        try:
            stmt = delete(User).where(User.id == user_id)
            await session.execute(stmt)
            await session.commit()
            print(f"User with ID {user_id} deleted.")
        except Exception as e:
            await session.rollback()
            print(f"Error deleting user: {e}")

async def insert_post_for_user(user_id: int, title: str, content: str):
    async with AsyncSessionLocal() as session:
        try:
            new_post = Post(title=title, content=content, user_id=user_id)
            session.add(new_post)
            await session.commit()
            await session.refresh(new_post)
            print(f"Inserted post '{title}' for user ID {user_id}")
        except Exception as e:
            await session.rollback()
            print(f"Error inserting post: {e}")

async def get_user_with_posts(user_id: int):
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(select(User).where(User.id == user_id))
            user = result.scalars().first()
            if user:
                await session.refresh(user)  # ensure posts are loaded
                user_data = UserWithPostsSchema.model_validate(user)
                print(json.dumps(user_data.model_dump(), indent=2))
            else:
                print(f"No user found with ID {user_id}")
        except Exception as e:
            print(f"Error fetching user with posts: {e}")

async def main():
    await insert_multiple_users([
        {"name": "Alice2", "email": "alice2@example.com"},
        {"name": "Bob2", "email": "bob2@example.com"}
    ])
    users = await fetch_users()
    display_users(users)
    await insert_post_for_user(4, "Hello", "This is Alice2's first post.")
    await get_user_with_posts(4)

if __name__ == "__main__":
    asyncio.run(main())