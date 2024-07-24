from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class CachedResult(Base):
    __tablename__ = "cached_results"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON, unique=True, index=True)
    output_data = Column(String, index=True)
