from scapy.all import *
from scapy.layers.inet import IP, UDP

# Define the target host and the ports you want to scan
src_port = RandShort()
target_ip = input("Insert target IP: ")
target_ports = input("Insert ports: ").split(",")
target_ports = [int(port) for port in target_ports]

# Perform the UDP port scan
answered, unanswered = sr(IP(dst=target_ip) / UDP(dport=target_ports), timeout=2, verbose=False)

# Print the open ports
for packet in answered:
    if packet[1].haslayer(UDP) and packet[1].getlayer(UDP).dport in target_ports:
        print(f"Port {packet[1].getlayer(UDP).dport} is open")
