from smb.SMBConnection import SMBConnection

client_name = input("Insert client name: ")
user = ""
password = ""
host = input("Host: ")
port = input("Port: ")
server_name = input("Server name: ")

s = SMBConnection(user, password, client_name, server_name, use_ntlm_v2=True)
if s.connect(host, port):
    print(s.listShares())