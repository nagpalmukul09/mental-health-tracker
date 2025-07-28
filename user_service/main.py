from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(title="User Service")

users = {}

class User(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register")
def register_user(user: User):
    user_id = str(uuid4())
    users[user_id] = user
    return {"user_id": user_id, "message": "User registered successfully"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id in users:
        return users[user_id]
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/")
def read_root():
	return {"message": "User Service is up"}
