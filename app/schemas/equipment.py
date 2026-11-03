from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class EquipmentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    location: str = Field(min_length=1, max_length=100)


class EquipmentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    location: str
    status: str = "unknown"
        