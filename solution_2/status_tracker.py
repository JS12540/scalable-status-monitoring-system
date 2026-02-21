import time
import queue
import feedparser

FEED_URL = "https://status.openai.com/history.atom"
POLL_INTERVAL = 60  # seconds (reasonable, not aggressive)

event_queue = queue.Queue()
seen_entries = set()


def fetch_feed():
    print("Checking OpenAI status feed...")
    feed = feedparser.parse(FEED_URL)

    for entry in feed.entries:
        entry_id = entry.get("id")

        if entry_id not in seen_entries:
            seen_entries.add(entry_id)

            event = {
                "timestamp": entry.get("updated"),
                "title": entry.get("title"),
                "summary": entry.get("summary"),
            }

            event_queue.put(event)


def consumer():
    while True:
        event = event_queue.get()

        ts = event["timestamp"]
        title = event["title"]
        summary = event["summary"]

        print(
            f"[{ts}] "
            f"Product/Event: {title}\n"
            f"Status: {summary}\n"
            f"{'-'*60}"
        )

        event_queue.task_done()


def main_loop():
    while True:
        try:
            fetch_feed()
        except Exception as e:
            print(f"Error fetching feed: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    import threading

    print("OpenAI Status Tracker Started\n")

    t = threading.Thread(target=consumer, daemon=True)
    t.start()

    main_loop()