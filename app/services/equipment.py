from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.equipment import Equipment
from app.schemas.equipment import EquipmentCreate


def create_equipment(db: Session, data: EquipmentCreate) -> Equipment:
    equipment = Equipment(
        name=data.name,
        location=data.location,
    )
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment


def list_equipments(db: Session) -> list[Equipment]:
    statement = select(Equipment).order_by(Equipment.created_at.desc())
    return list(db.scalars(statement).all())


def get_equipment(db: Session, equipment_id: UUID) -> Equipment | None:
    return db.get(Equipment, equipment_id)
