
from fastapi.testclient import TestClient
from uuid import uuid4

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_equipment():
    response = client.post(
        "/equipment",
        json={
            "name": "Pompe hydraulique P-101",
            "location": "Atelier A",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Pompe hydraulique P-101"
    assert data["location"] == "Atelier A"
    assert data["status"] == "unknown"
    assert "id" in data


def test_create_equipment_rejects_empty_name():
    response = client.post(
        "/equipment",
        json={
            "name": "",
            "location": "Atelier A",
        },
    )

    assert response.status_code == 422


def test_get_existing_equipment():
    created = client.post(
        "/equipment",
        json={
            "name": "Pompe P-102",
            "location": "Atelier B",
        },
    )
    equipment_id = created.json()["id"]

    response = client.get(f"/equipment/{equipment_id}")

    assert response.status_code == 200
    assert response.json()["id"] == equipment_id
    assert response.json()["name"] == "Pompe P-102"


def test_get_unknown_equipment_returns_404():
    unknown_id = uuid4()

    response = client.get(f"/equipment/{unknown_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Equipment not found"

