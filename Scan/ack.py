from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP

src_port = RandShort()
target_ip = input("Insert target IP: ")
target_ports = input("Insert ports: ").split(",")
target_ports = [int(port) for port in target_ports]

for port in target_ports:
    response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="A"), timeout=1, verbose=0)
    if response is None:
        print(f"Port {port} is filtered (no response)")

    elif response.haslayer(TCP) and response[TCP].flags == 0x04:
        print(f"Port {port} is closed")

    elif response.haslayer(TCP) and response[TCP].flags == 0x14:
        print(f"Port {port} is open")

    elif response.haslayer(ICMP):
        if int(response[ICMP].type) == 3 and int(response[ICMP].code) in [1, 2, 3, 9, 10, 13]:
            print(f"Port {port} is filtered by a firewall")

        elif int(response[ICMP].type) == 3 and int(response[ICMP].code) == 0:
            print(f"Port {port} is closed")

        else:
            print("Unknown ICMP response")

    else:
        print("Unknown response")
