import binascii, hashlib, sys

if len(sys.argv) != 3:
    print("[-] Usage: ntlm.py <hashes_file> <dict_file>")
    exit()

hashes = open(sys.argv[1])
dictFile = open(sys.argv[2])

for account in hashes:
    for passwd in dictFile:
        hashLine = account.split(":")[3]
        ntlm_hash = binascii.hexlify(hashlib.new("md4", passwd.encode("utf-16le")).digest())

        if ntlm_hash == hashLine:
            print("[+] Hash Found!! Username: %s Password: %s" % (account.split(":")[0], passwd))
