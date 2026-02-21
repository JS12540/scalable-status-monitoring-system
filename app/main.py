from fastapi import FastAPI, Request
from app.queue import publish_event

app = FastAPI()

@app.post("/webhook/status")
async def receive_status(request: Request):
    payload = await request.json()

    event = {
        "source": payload.get("source", "unknown"),
        "product": payload.get("product", "unknown"),
        "status": payload.get("status", "unknown"),
        "timestamp": payload.get("timestamp"),
    }

    publish_event(event)

    return {"message": "Event received"}