from scapy.all import *
from scapy.layers.inet import IP, TCP

target_ip = input("Insert target IP: ")
target_ports = input("Insert ports: ").split(",")
target_ports = [int(port) for port in target_ports]

for port in target_ports:
    packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    response = sr1(packet, timeout=1, verbose=0)

    if response:
        if response.haslayer(TCP) and response[TCP].flags == "SA":
            print(f"Port {port} open")
        else:
            print(f"Port {port} closed")
    else:
        print(f"No response from port {port}")
