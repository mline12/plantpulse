from uuid import UUID, uuid4

from app.schemas.equipment import EquipmentCreate, EquipmentRead


_equipments: dict[UUID, EquipmentRead] = {}


def create_equipment(data: EquipmentCreate) -> EquipmentRead:
    equipment = EquipmentRead(
        id=uuid4(),
        name=data.name,
        location=data.location,
    )
    _equipments[equipment.id] = equipment
    return equipment


def list_equipments() -> list[EquipmentRead]:
    return list(_equipments.values())


def get_equipment(equipment_id: UUID) -> EquipmentRead | None:
    return _equipments.get(equipment_id)