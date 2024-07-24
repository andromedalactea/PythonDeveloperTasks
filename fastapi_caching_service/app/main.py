from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Simulate external transformer function
def transformer_function(string: str) -> str:
    return string.upper()

# Endpoint to create a new payload
@app.post("/payload/", response_model=schemas.CachedResult)
def create_payload(payload: schemas.PayloadCreate, db: Session = Depends(get_db)):
    input_data = {"list_1": payload.list_1, "list_2": payload.list_2}
    cached_result = crud.get_cached_result(db, input_data=input_data)
    
    if cached_result:
        return cached_result
    
    transformed_list_1 = [transformer_function(s) for s in payload.list_1]
    transformed_list_2 = [transformer_function(s) for s in payload.list_2]
    
    interleaved_output = ", ".join([val for pair in zip(transformed_list_1, transformed_list_2) for val in pair])
    
    return crud.create_cached_result(db, input_data=input_data, output_data=interleaved_output)

# Endpoint to read a payload by ID
@app.get("/payload/{id}", response_model=schemas.CachedResult)
def read_payload(id: int, db: Session = Depends(get_db)):
    cached_result = db.query(models.CachedResult).filter(models.CachedResult.id == id).first()
    if cached_result is None:
        raise HTTPException(status_code=404, detail="Payload not found")
    return cached_result
