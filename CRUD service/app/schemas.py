from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id: int

class User(UserBase):
    id: int

    class Config:
        orm_mode = True