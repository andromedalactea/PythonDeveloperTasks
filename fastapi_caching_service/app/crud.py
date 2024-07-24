from sqlalchemy.orm import Session
from . import models, schemas

def get_cached_result(db: Session, input_data: dict):
    return db.query(models.CachedResult).filter(models.CachedResult.input_data == input_data).first()

def create_cached_result(db: Session, input_data: dict, output_data: str):
    db_result = models.CachedResult(input_data=input_data, output_data=output_data)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
