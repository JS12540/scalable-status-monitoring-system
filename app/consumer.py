from app.queue import consume_event

def start_consumer():
    print("Consumer started...\n")

    while True:
        event = consume_event()

        print(
            f"[{event['timestamp']}] "
            f"Source: {event['source']} | "
            f"Product: {event['product']}\n"
            f"Status: {event['status']}\n"
            f"{'-'*60}"
        )


if __name__ == "__main__":
    start_consumer()