from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/logs")
def get_logs():
    # Sample dummy logs
    return [
        {"user": "alice", "action": "login", "time": "2025-06-11T13:00:00"},
        {"user": "bob", "action": "file_access", "file": "confidential.pdf", "time": "2025-06-11T13:05:00"}
    ]
