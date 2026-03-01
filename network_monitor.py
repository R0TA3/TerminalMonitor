# network_monitor.py
from scapy.all import sniff, IP, TCP, UDP
from colorama import Fore, Style

PORTS_SUSPICIOUS = [22, 23, 3389]

def process_packet(packet):
    src_ip = packet[IP].src if packet.haslayer(IP) else "N/A"
    dst_ip = packet[IP].dst if packet.haslayer(IP) else "N/A"
    protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "OTHER"
    dst_port = packet[TCP].dport if packet.haslayer(TCP) else packet[UDP].dport if packet.haslayer(UDP) else 0

    severity = "LOW"
    if dst_port in PORTS_SUSPICIOUS:
        severity = "HIGH"
        print(Fore.RED + f"[ALERT] Suspicious {protocol} packet {src_ip} -> {dst_ip}:{dst_port}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"[INFO] {protocol} packet {src_ip} -> {dst_ip}:{dst_port}" + Style.RESET_ALL)

def start_network_monitor():
    print("Network monitoring started...")
    sniff(prn=process_packet, store=False)
