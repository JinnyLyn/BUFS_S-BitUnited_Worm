#!/usr/bin/python3.12

from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

flag = open("/flag", "rb").read()

key = get_random_bytes(256)
ciphertext = strxor(flag, key[:len(flag)])

print(f"Flag Ciphertext (b64): {b64encode(ciphertext).decode()}")

while True:
    plaintext = b64decode(input("Plaintext (b64): "))
    ciphertext = strxor(plaintext, key[:len(plaintext)])
    print(f"Ciphertext (b64): {b64encode(ciphertext).decode()}")
