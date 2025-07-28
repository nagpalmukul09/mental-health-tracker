from fastapi.testclient import TestClient
from journal_service.main import app

client = TestClient(app)

def test_add_entry():
    payload = {
        "user_id": "user123",
        "content": "This is my first journal entry."
    }
    response = client.post("/journal", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Journal entry added"}

def test_get_entries():
    user_id = "user123"
    response = client.get(f"/journal/{user_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
