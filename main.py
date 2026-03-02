import threading
import queue
import time
from system_monitor import monitor_logs
from network_monitor import monitor_network
from correlation import analyze_event
from database import log_event

event_queue = queue.Queue()

def event_worker():
    while True:
        event = event_queue.get()
        if event:
            log_event(event)
            analyze_event(event)

def main():
    print("[+] TerminalMonitor SIEM Engine Starting...")

    threading.Thread(target=monitor_logs, args=(event_queue,), daemon=True).start()
    threading.Thread(target=monitor_network, args=(event_queue,), daemon=True).start()
    threading.Thread(target=event_worker, daemon=True).start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
