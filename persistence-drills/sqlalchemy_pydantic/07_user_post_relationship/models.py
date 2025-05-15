from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from pydantic import BaseModel, EmailStr, ConfigDict

Base = declarative_base()
engine = create_engine("sqlite:///users.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Relationship: one user has many posts
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

    class Config:
        from_attributes = True

class EmailUpdateSchema(BaseModel):
    email: EmailStr
    
class PostSchema(BaseModel):
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)