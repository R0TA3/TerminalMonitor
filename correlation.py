from detection_engine import *
from alert_engine import raise_alert

def analyze_event(event):

    brute, ip = detect_bruteforce(event)
    if brute:
        raise_alert("SSH BRUTE FORCE", ip)

    scan, ip = detect_port_scan(event)
    if scan:
        raise_alert("PORT SCAN", ip)

    flood, ip = detect_icmp_flood(event)
    if flood:
        raise_alert("ICMP FLOOD", ip)
