from fastapi import FastAPI
from backend.debate_generator import generate_debate
from pydantic import BaseModel

app = FastAPI()

class DebateRequest(BaseModel):
    topic: str

@app.post("/generate-debate/")
def generate_debate_api(request: DebateRequest):
    arguments = generate_debate(request.topic)
    return {"topic": request.topic, "arguments": arguments}

