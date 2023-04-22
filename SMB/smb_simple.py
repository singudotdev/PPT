from smb.SMBConnection import SMBConnection

server_name = input("Insert server name: ")
client_name = input("Insert client name: ")
user = input("Insert username: ")
password = input("Insert password: ")

s = SMBConnection(user, password, client_name, server_name, use_ntlm_v2=True)
s.connect(input("Insert IP: "), input("Insert port: "))
print(s.listShares())
