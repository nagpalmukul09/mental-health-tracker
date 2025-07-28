from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Journal Service",
    description="This service allows users to write and retrieve private journal entries.",
    version="1.0.0"
)

journal_entries = {}

class JournalEntry(BaseModel):
    user_id: str
    content: str

@app.post("/journal")
def add_entry(entry: JournalEntry):
    if entry.user_id not in journal_entries:
        journal_entries[entry.user_id] = []
    journal_entries[entry.user_id].append(entry)
    return {"message": "Journal entry added"}

@app.get("/journal/{user_id}")
def get_entries(user_id: str):
    return journal_entries.get(user_id, [])
