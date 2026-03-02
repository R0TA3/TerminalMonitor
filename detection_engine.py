from collections import defaultdict
import time
import re

failed_logins = defaultdict(list)

def extract_ip(text):
    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)
    if match:
        return match.group()
    return None

def detect_bruteforce(event):
    if event.message and "Failed password" in event.message:
        ip = extract_ip(event.message)
        now = time.time()

        failed_logins[ip].append(now)
        failed_logins[ip] = [t for t in failed_logins[ip] if now - t < 30]

        print(f"[DEBUG] Failed logins from {ip}: {len(failed_logins[ip])}")

        if len(failed_logins[ip]) >= 5:
            return True, ip

    return False, None

def detect_port_scan(event):
    return False, None

def detect_icmp_flood(event):
    return False, None
