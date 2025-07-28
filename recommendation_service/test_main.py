from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_recommendation_low():
    response = client.get("/recommendations/1")
    assert response.status_code == 200
    assert "walk" in response.json()["tip"]

def test_get_recommendation_medium():
    response = client.get("/recommendations/3")
    assert response.status_code == 200
    assert "journal" in response.json()["tip"]

def test_get_recommendation_high():
    response = client.get("/recommendations/5")
    assert response.status_code == 200
    assert "vibes" in response.json()["tip"]
