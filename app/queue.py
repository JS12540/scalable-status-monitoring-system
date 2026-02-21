import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

QUEUE_NAME = "status_events"


def publish_event(event: dict):
    r.rpush(QUEUE_NAME, json.dumps(event))


def consume_event():
    _, data = r.blpop(QUEUE_NAME)
    return json.loads(data)