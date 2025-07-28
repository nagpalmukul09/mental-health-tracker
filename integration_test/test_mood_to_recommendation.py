import pytest
import httpx

BASE_RECOMMEND_URL = "http://localhost:8004"

@pytest.mark.asyncio
async def test_recommendation_based_on_mood():
    mood_level = 3  # simulate a normal mood level
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_RECOMMEND_URL}/recommendations/{mood_level}")
        assert response.status_code == 200
        assert "tip" in response.json()
