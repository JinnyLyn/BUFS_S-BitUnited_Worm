#!/usr/bin/python3.12
from pwn import *
import base64

# 풀이환경 프로세스임.
r = process('/challenge/run')

r.recvuntil(b'Flag Ciphertext (b64): ')
flag_ct_b64 = r.recvline().strip()
flag_ct = base64.b64decode(flag_ct_b64)
flag_length = len(flag_ct)

plaintext = b'\x00' * 256
plaintext_b64 = base64.b64encode(plaintext).decode()

r.sendlineafter(b'Plaintext (b64): ', plaintext_b64.encode())

r.recvuntil(b'Ciphertext (b64): ')
key_ct_b64 = r.recvline().strip()
key_ct = base64.b64decode(key_ct_b64)

key = key_ct[:flag_length]

flag = bytes([fc ^ kc for fc, kc in zip(flag_ct, key)])
print(f"Flag: {flag.decode()}")

r.close()
