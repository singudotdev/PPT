from scapy.all import *
from scapy.layers.inet import IP, TCP

src_port = RandShort()
target_ip = input("Insert target IP: ")
target_ports = input("Insert ports: ").split(",")
target_ports = [int(port) for port in target_ports]

answered, unanswered = sr(
    IP(dst=target_ip) /
    TCP(sport=RandShort(), dport=target_ports, flags="S"),
    timeout=1, verbose=False
)

for packet in answered:
    if packet[1].haslayer(TCP) and packet[1].getlayer(TCP).flags == 0x12:
        print(f"Port {packet[0].dport} open")
