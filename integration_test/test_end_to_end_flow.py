import pytest
import httpx
import uuid

BASE_USER_URL = "http://localhost:8001"
BASE_MOOD_URL = "http://localhost:8002"
BASE_JOURNAL_URL = "http://localhost:8003"
BASE_RECOMMEND_URL = "http://localhost:8004"
BASE_NOTIFY_URL = "http://localhost:8005"

@pytest.mark.asyncio
async def test_full_user_flow():
    # Step 1: Register user
    user_data = {
        "username": "testuser",
        "email": f"test{uuid.uuid4()}@example.com",
        "password": "securepass"
    }
    async with httpx.AsyncClient() as client:
        user_response = await client.post(f"{BASE_USER_URL}/register", json=user_data)
        assert user_response.status_code == 200
        user_id = user_response.json()["user_id"]

        # Step 2: Log mood
        mood_data = {"user_id": user_id, "mood_level": 3, "notes": "Feeling okay"}
        mood_response = await client.post(f"{BASE_MOOD_URL}/moods", json=mood_data)
        assert mood_response.status_code == 200

        # Step 3: Add journal entry
        journal_data = {"user_id": user_id, "content": "Reflected on my mood today"}
        journal_response = await client.post(f"{BASE_JOURNAL_URL}/journal", json=journal_data)
        assert journal_response.status_code == 200

        # Step 4: Get recommendation based on mood_level=3
        rec_response = await client.get(f"{BASE_RECOMMEND_URL}/recommendations/3")
        assert rec_response.status_code == 200
        tip = rec_response.json()["tip"]

        # Step 5: Send notification
        notification = {"user_id": user_id, "message": f"Daily tip: {tip}"}
        notify_response = await client.post(f"{BASE_NOTIFY_URL}/notify", json=notification)
        assert notify_response.status_code == 200
