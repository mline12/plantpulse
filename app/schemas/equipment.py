from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class EquipmentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    location: str = Field(min_length=1, max_length=100)

class EquipmentRead(BaseModel):
    id: UUID
    name: str
    location: str
    status: str = "unknown"
        