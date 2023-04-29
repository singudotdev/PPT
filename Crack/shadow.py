import os, sys
import crypt
import codecs
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
