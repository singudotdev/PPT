import select
import socket
import sys
from subprocess import Popen, PIPE

if len(sys.argv) != 3:
    print("[-] Usage: bind.py <interface> <port>")
