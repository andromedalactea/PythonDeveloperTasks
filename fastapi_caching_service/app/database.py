from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  


# Create engine to manage database connections.
# `connect_args={"check_same_thread": False}` is necessary for SQLite to allow usage across multiple threads.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory bound to the engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions.
Base = declarative_base()

def get_db():
    # Create a new session using the session factory.
    db = SessionLocal()
    try:
        # This allows the caller to use the session for database operations.
        yield db
    finally:
        # Ensure the session is closed after use to release database connections.
        db.close()
