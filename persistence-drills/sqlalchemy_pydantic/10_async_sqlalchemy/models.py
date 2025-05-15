from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel, EmailStr, ConfigDict

DATABASE_URL = "postgresql+asyncpg://rishabh:123456@localhost/user_post_management"

Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

class UserSchema(BaseModel):
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class EmailUpdateSchema(BaseModel):
    email: EmailStr

class PostSchema(BaseModel):
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class PostOutSchema(BaseModel):
    id: int
    title: str
    content: str

    model_config = ConfigDict(from_attributes=True)

class UserWithPostsSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    posts: list[PostOutSchema]

    model_config = ConfigDict(from_attributes=True)