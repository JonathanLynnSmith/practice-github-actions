from fastapi import FastAPI
from pydantic import BaseModel
from linter import validate_commit_message

app = FastAPI()

class CommitMessage(BaseModel):
    message: str

@app.post("/validate")
def validate_commit(commit: CommitMessage):
    valid, reason = validate_commit_message(commit.message)
    return {"valid": valid, "reason": reason}

@app.get("/")
def read_root():
    return {"message": "Welcome to the commit message linter API! Use /validate to validate a commit message."}
