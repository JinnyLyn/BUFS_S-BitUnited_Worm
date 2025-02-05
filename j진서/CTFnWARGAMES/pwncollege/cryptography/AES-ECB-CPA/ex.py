import base64
from pwn import *

context.log_level = 'error'

def exploit():
    r = process('/challenge/run')
    flag = []
    i = 0

    while True:
        r.sendlineafter(b'Choice? ', b'2')
        r.sendlineafter(b'Index?', str(i).encode())
        r.sendlineafter(b'Length? ', b'1')
        ct_line = r.recvline().decode().strip()
        ct_flag = base64.b64decode(ct_line.split(': ')[1])
        ct_flag_block = ct_flag[:16]

        found = False
        for b in range(32, 127):
            r.sendlineafter(b'Choice? ', b'1')
            r.sendlineafter(b'Data? ', chr(b).encode())
            ct_test_line = r.recvline().decode().strip()
            ct_test = base64.b64decode(ct_test_line.split(': ')[1])
            ct_test_block = ct_test[:16]

            if ct_test_block == ct_flag_block:
                flag.append(chr(b))
                found = True
                break

        if not found:
            print(f"Failed at index {i}. Flag text so far: {''.join(flag)}")
            break

        print(f"Progress: {''.join(flag)}")
        i += 1

        if flag[-1] == '}':
            break

    r.close()
    return ''.join(flag)

if __name__ == '__main__':
    flag = exploit()
    print(f'Flag: {flag}')
