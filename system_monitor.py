from events import Event
from datetime import datetime
import time

def monitor_logs(event_queue):
    print("[+] System log monitoring started (TEST MODE)")

    while True:
        fake_line = "Failed password for root from 10.0.0.5 port 22 ssh2"

        event = Event(
            timestamp=str(datetime.now()),
            source="system",
            event_type="auth_fail",
            message=fake_line,
            severity="medium"
        )

        print("[*] Injecting test auth failure event")
        event_queue.put(event)

        time.sleep(3)
