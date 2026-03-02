from scapy.all import sniff, IP
from events import Event
from datetime import datetime

def packet_handler(packet, event_queue):
    if IP in packet:
        event = Event(
            timestamp=str(datetime.now()),
            source="network",
            event_type="packet",
            src_ip=packet[IP].src,
            dst_ip=packet[IP].dst,
            protocol=packet.proto,
            severity="low"
        )
        event_queue.put(event)

def monitor_network(event_queue):
    print("[+] Network monitoring started")
    sniff(prn=lambda pkt: packet_handler(pkt, event_queue), store=0)
