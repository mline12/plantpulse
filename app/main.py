from uuid import UUID

from fastapi import FastAPI, HTTPException, status

from app.schemas.equipment import EquipmentCreate, EquipmentRead
from app.services.equipment import (
    create_equipment,
    get_equipment,
    list_equipments,
)

app = FastAPI(
    title="PlantPulse API",
    description="Industrial telemetry and monitoring API",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/equipment",
    response_model=EquipmentRead,
    status_code=status.HTTP_201_CREATED,
)
def add_equipment(data: EquipmentCreate) -> EquipmentRead:
    return create_equipment(data)


@app.get("/equipment", response_model=list[EquipmentRead])
def get_equipments() -> list[EquipmentRead]:
    return list_equipments()


@app.get("/equipment/{equipment_id}", response_model=EquipmentRead)
def get_equipment_by_id(equipment_id: UUID) -> EquipmentRead:
    equipment = get_equipment(equipment_id)

    if equipment is None:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found",
        )

    return equipment
