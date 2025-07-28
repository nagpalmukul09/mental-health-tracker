from fastapi.testclient import TestClient
from notification_service.main import app

client = TestClient(app)

def test_send_notification():
    payload = {
        "user_id": "user_123",
        "message": "Test notification"
    }
    response = client.post("/notify", json=payload)
    assert response.status_code == 200
    assert "Notification queued for user" in response.json()["message"]

def test_list_notifications():
    response = client.get("/notifications")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
