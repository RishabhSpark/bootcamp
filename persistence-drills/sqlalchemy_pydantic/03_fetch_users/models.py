from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel, EmailStr

Base = declarative_base()
engine = create_engine("sqlite:///users.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class UserSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
