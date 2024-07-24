import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base

# Configure the test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new database session for testing
Base.metadata.create_all(bind=engine)

# Dependency override to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Function to clean the database before each test
@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Test the creation of a new user
def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "john.doe@example.com", "age": 30})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"
    assert data["age"] == 30

# Test the retrieval of a user by ID
def test_read_user():
    # First, create a new user
    response = client.post("/users/", json={"name": "Jane Doe", "email": "jane.doe@example.com", "age": 25})
    data = response.json()
    user_id = data["id"]

    # Now, retrieve the user by ID
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@example.com"
    assert data["age"] == 25

# Test the retrieval of multiple users with pagination
def test_read_users():
    # Create multiple users
    client.post("/users/", json={"name": "User1", "email": "user1@example.com", "age": 20})
    client.post("/users/", json={"name": "User2", "email": "user2@example.com", "age": 22})

    # Retrieve users with pagination
    response = client.get("/users/?skip=0&limit=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "User1"
    assert data[1]["name"] == "User2"

# Test the update of an existing user
def test_update_user():
    # First, create a new user
    response = client.post("/users/", json={"name": "Old Name", "email": "old.email@example.com", "age": 40})
    data = response.json()
    user_id = data["id"]

    # Now, update the user
    response = client.put(f"/users/{user_id}", json={"id": user_id, "name": "New Name", "email": "new.email@example.com", "age": 41})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "New Name"
    assert data["email"] == "new.email@example.com"
    assert data["age"] == 41

# Test the deletion of a user by ID
def test_delete_user():
    # First, create a new user
    response = client.post("/users/", json={"name": "User To Delete", "email": "delete.me@example.com", "age": 50})
    data = response.json()
    user_id = data["id"]

    # Now, delete the user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

    # Verify the user has been deleted
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"
