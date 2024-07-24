from pydantic import BaseModel

# Base schema for user data, containing common fields
class UserBase(BaseModel):
    name: str  
    email: str  
    age: int  

# Schema for creating a new user
class UserCreate(UserBase):
    pass  # No additional fields, same structure as UserBase

# Schema for updating an existing user
class UserUpdate(UserBase):
    id: int 

# Schema for representing a user
class User(UserBase):
    id: int  

    # Configuration class to indicate that the model should be compatible with ORM models
    class Config:
        from_attributes = True  # Enables Pydantic to work with SQLAlchemy ORM models
