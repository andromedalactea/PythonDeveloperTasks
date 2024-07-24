from sqlalchemy.orm import Session
from . import models, schemas

# Function to retrieve a cached result based on input data
def get_cached_result(db: Session, input_data: dict):
    # Query the CachedResult table to find a record with matching input_data
    return db.query(models.CachedResult).filter(models.CachedResult.input_data == input_data).first()

# Function to create a new cached result
def create_cached_result(db: Session, input_data: dict, output_data: str):
    # Create a new CachedResult instance with the provided input and output data
    db_result = models.CachedResult(input_data=input_data, output_data=output_data)
    db.add(db_result)  
    db.commit()  
    db.refresh(db_result) 
    return db_result