import crypt
import argparse


def bruteForce(cryptPass, user):
    dicFile = open("dic.txt", "r")
    hashType = cryptPass.split("$")[1]

    if hashType == "6":
        print("[+] Hash type SHA-512...")
        salt = cryptPass.split("$")[2]
        salt = "$" + hashType + "$" + salt + "$"

        for passwd in dicFile.readlines():
            passwd = passwd.strip("\n")
            cryptWord = crypt.crypt(passwd, salt)

            if cryptWord == cryptPass:
                print(f"Found password for user {user}: {passwd}")


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Simple bruteforcer for /etc/shadow")
    parse.add_argument("-f", dest='shadowFile', help="Shadow file location")
    argus = parse.parse_args()

    if argus.shadowFile is None:
        parse.print_help()
        exit()

    else:
        passFile = open(argus.shadowFile, "r")
        for line in passFile.readlines():
            line = line.replace("\n", "").split(":")
            if not line[1] in ["x", "*", "!"]:
                user = line[0]
                cryptPass = line[1]
                bruteForce(cryptPass, user)
