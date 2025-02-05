#!/usr/bin/python3.12
from pwn import *

try:
    while True:
        a = str(input("first one: ")).strip()
        b = str(input("second one: ")).strip()

        a_bytes = a.encode()
        b_bytes = b.encode()

        result = xor(a_bytes, b_bytes)

        print(result)
        print(result.decode(errors='ignore'))
except KeyboardInterrupt:
    print("\nExiting... Goodbye")
