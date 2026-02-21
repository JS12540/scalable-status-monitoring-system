import requests
from datetime import datetime
import time
import random

URL = "http://localhost:8000/webhook/status"

products = [
    "OpenAI API - Chat Completions",
    "OpenAI API - Responses",
    "OpenAI API - Embeddings",
]

statuses = [
    "Operational",
    "Degraded performance",
    "Partial outage",
    "Major outage",
]

while True:
    payload = {
        "source": "OpenAI Status (Mock)",
        "product": random.choice(products),
        "status": random.choice(statuses),
        "timestamp": datetime.utcnow().isoformat(),
    }

    requests.post(URL, json=payload)

    print("Sent mock event")
    time.sleep(5)