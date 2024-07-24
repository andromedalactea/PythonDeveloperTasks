from sqlalchemy import Column, Integer, String, JSON
from .database import Base

# Define the CachedResult model that represents the cached_results table in the database
class CachedResult(Base):
    __tablename__ = "cached_results"  # Specifies the name of the table in the database

    # Define the columns of the cached_results table
    id = Column(Integer, primary_key=True, index=True) 
    input_data = Column(JSON, unique=True, index=True)  
    output_data = Column(String, index=True) 
