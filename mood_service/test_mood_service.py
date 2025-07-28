from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_log_mood():
    payload = {
        "user_id": "user123",
        "mood_level": 5,
        "notes": "Feeling good"
    }
    response = client.post("/moods", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Mood logged successfully"}

def test_get_moods():
    user_id = "user123"
    response = client.get(f"/moods/{user_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
