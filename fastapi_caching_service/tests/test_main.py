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

# Test the creation of a new payload
def test_create_payload():
    response = client.post("/payload/", json={"list_1": ["first string", "second string"], "list_2": ["other string", "another string"]})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["input_data"] == {
        "list_1": ["first string", "second string"],
        "list_2": ["other string", "another string"]
    }
    assert data["output_data"] == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING"

# Test the retrieval of a payload by ID
def test_read_payload():
    # First, create a new payload
    response = client.post("/payload/", json={"list_1": ["first string", "second string"], "list_2": ["other string", "another string"]})
    data = response.json()
    payload_id = data["id"]

    # Now, retrieve the payload by ID
    response = client.get(f"/payload/{payload_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload_id
    assert data["input_data"] == {
        "list_1": ["first string", "second string"],
        "list_2": ["other string", "another string"]
    }
    assert data["output_data"] == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING"
