from pwn import *
import base64

def b64decode_xor(key_b64, cipher_b64):
    key = base64.b64decode(key_b64)
    cipher = base64.b64decode(cipher_b64)

    plaintext = bytes(a ^ b for a, b in zip(key, cipher))

    return plaintext.decode(errors='ignore')

key_b64 = str(input('first one: ')).strip()
cipher_b64 = str(input('second one: ')).strip()

flag = b64decode_xor(key_b64, cipher_b64)
print('Decrypted Flag: ', flag)
