from sqlalchemy import Column, Integer, String
from .database import Base

# Define the User model that represents the users table in the database
class User(Base):
    __tablename__ = "users"  

    # Define the columns of the users table
    id = Column(Integer, primary_key=True, index=True)  # Primary key, unique identifier
    name = Column(String, index=True) 
    email = Column(String, unique=True, index=True) 
    age = Column(Integer)  
