# main.py
import threading
from system_monitor import start_system_monitor
from network_monitor import start_network_monitor

if __name__ == "__main__":
    # System monitor runs in a separate thread
    t1 = threading.Thread(target=start_system_monitor)
    t1.start()

    # Network monitor runs in main thread
    start_network_monitor()
