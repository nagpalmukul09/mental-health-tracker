from fastapi.testclient import TestClient
from user_service.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_register_user():
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert "user_id" in response.json()
    assert response.json()["message"] == "User registered successfully"
