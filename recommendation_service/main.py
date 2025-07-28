from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Recommendation Service",
    description="This service provides wellness tips based on mood level.",
    version="1.0.0"
)

@app.get("/recommendations/{mood_level}")
def get_recommendation(mood_level: int):
    if mood_level <= 2:
        return {"tip": "Try taking a walk or speaking with someone you trust."}
    elif mood_level == 3:
        return {"tip": "You're doing okay! Take a moment to journal your thoughts."}
    else:
        return {"tip": "Keep up the good vibes! Maybe help a friend feel better too."}
