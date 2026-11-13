from unittest.mock import Mock

import pytest

from app.schemas.equipment import EquipmentCreate
from app.services.equipment import create_equipment

def test_create_equipment_rolls_back_on_commit_error():
    db = Mock()
    db.commit.side_effect = RuntimeError("Database error")

    data = EquipmentCreate(
        name = "Pompe P-101",
        location = "Atelier A",
    )

    with pytest.raises(RuntimeError, match="Database error"):
        create_equipment(db, data)
    db.rollback.assert_called_once()
    