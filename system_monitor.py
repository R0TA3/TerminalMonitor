from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, Style
import time
import re
import os

class SystemLogHandler(FileSystemEventHandler):
    def process(self, path):
        if not os.path.exists(path):
            return
        try:
            with open(path, "r") as f:
                lines = f.readlines()[-10:]  # last 10 lines
                for line in lines:
                    severity = "LOW"
                    if re.search(r"Failed|error|fail|authentication", line, re.IGNORECASE):
                        severity = "HIGH"
                        print(Fore.RED + "[ALERT] " + line.strip() + Style.RESET_ALL)
                    elif re.search(r"succeeded|opened|sudo", line, re.IGNORECASE):
                        severity = "MEDIUM"
                        print(Fore.YELLOW + "[NOTICE] " + line.strip() + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + "[INFO] " + line.strip() + Style.RESET_ALL)
        except Exception as e:
            print(Fore.YELLOW + f"[WARNING] Could not read {path}: {e}" + Style.RESET_ALL)

    def on_modified(self, event):
        if not event.is_directory:
            self.process(event.src_path)

def start_system_monitor():
    paths_to_monitor = [
        "/var/log/syslog",
        "/var/log/boot.log",
        "/var/log/dpkg.log",
    ]

    existing_paths = [p for p in paths_to_monitor if os.path.exists(p)]
    if not existing_paths:
        print(Fore.RED + "No log files found to monitor. Exiting system monitor." + Style.RESET_ALL)
        return

    event_handler = SystemLogHandler()
    observer = Observer()

    for path in existing_paths:
        print(f"Monitoring {path} ...")
        observer.schedule(event_handler, path=path, recursive=False)

    observer.start()
    print("System log monitoring started...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
