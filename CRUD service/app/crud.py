from sqlalchemy.orm import Session
from . import models, schemas

# Retrieve a user by ID from the database
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Retrieve a list of users from the database with optional pagination
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create a new user in the database
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Update an existing user in the database
def update_user(db: Session, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.age = user.age
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user from the database by ID
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
