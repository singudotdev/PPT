from smb.SMBConnection import SMBConnection
from twisted.internet import defer, reactor


@defer.inlineCallbacks
def connect_to_smb():
    username = input("Username: ")
    password = input("Password: ")
    client_name = input("Client name: ")
    server_name = input("Server name: ")
    server_ip = input("Server IP: ")

    conn = SMBConnection(username, password, client_name, server_name)
    yield conn.connect(server_ip, 139)
    print('Connected to SMB service')

    # Perform SMB operations here
    files = conn.listPath('share', '/')
    for file in files:
        print(file.filename)

    conn.close()
    print('Disconnected from SMB service')


if __name__ == '__main__':
    reactor.callWhenRunning(connect_to_smb)
    reactor.run()
