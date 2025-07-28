from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Notification Service",
    description="This service simulates notifications being sent to users.",
    version="1.0.0"
)

notifications = []

class Notification(BaseModel):
    user_id: str
    message: str

@app.post("/notify")
def send_notification(note: Notification):
    notifications.append(note)
    return {"message": f"Notification queued for user {note.user_id}"}

@app.get("/notifications")
def list_notifications():
    return notifications

@app.get("/health")
def health_check():
    return {"status": "ok"}
