from pydantic import BaseModel
from typing import List

class PayloadCreate(BaseModel):
    list_1: List[str]
    list_2: List[str]

class CachedResult(BaseModel):
    id: int
    input_data: dict
    output_data: str

    class Config:
        from_attributes = True