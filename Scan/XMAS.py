from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP

src_port = RandShort()
target_ip = input("Insert target IP: ")
target_ports = input("Insert ports: ").split(",")
target_ports = [int(port) for port in target_ports]

for port in target_ports:
    response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="FPU"), timeout=10)

    if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
        print("Port {} closed".format(port))
    elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
        print("Port {} open".format(port))
    else:
        print("Port {} filtered".format(port))
