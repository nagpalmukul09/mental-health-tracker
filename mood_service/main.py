from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mood Tracker Service")

moods = {}

class Mood(BaseModel):
    user_id: str
    mood_level: int
    notes: str

@app.post("/moods")
def log_mood(mood: Mood):
    if mood.user_id not in moods:
        moods[mood.user_id] = []
    moods[mood.user_id].append(mood)
    return {"message": "Mood logged successfully"}

@app.get("/moods/{user_id}")
def get_moods(user_id: str):
    return moods.get(user_id, [])
 
@app.get("/health")
def health_check():
	return{"status": "ok"}
