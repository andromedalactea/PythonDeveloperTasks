from pydantic import BaseModel
from typing import List

# Pydantic model for the payload creation input
class PayloadCreate(BaseModel):
    list_1: List[str]  
    list_2: List[str]  

# Pydantic model for the cached result
class CachedResult(BaseModel):
    id: int  
    input_data: dict  
    output_data: str  

    class Config:
        from_attributes = True  # Enable compatibility with ORM models
