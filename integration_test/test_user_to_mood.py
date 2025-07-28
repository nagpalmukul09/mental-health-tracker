import pytest
import asyncio
import httpx

BASE_USER_URL = "http://localhost:8001"
BASE_MOOD_URL = "http://localhost:8002"

@pytest.mark.asyncio
async def test_user_register_and_log_mood():
    async with httpx.AsyncClient() as client:
        # Register a new user
        user_payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass"
        }
        user_response = await client.post(f"{BASE_USER_URL}/register", json=user_payload)
        assert user_response.status_code == 200
        user_id = user_response.json()["user_id"]

        # Log mood for this user
        mood_payload = {
            "user_id": user_id,
            "mood_level": 4,
            "notes": "Feeling good"
        }
        mood_response = await client.post(f"{BASE_MOOD_URL}/moods", json=mood_payload)
        assert mood_response.status_code == 200
        assert "Mood logged successfully" in mood_response.json()["message"]
