from pwn import *

p = process(['python3', 'run.py'], stdin=PTY)


def extract_char(line):
    stripped_line = line.strip()
    print(f'received line: {stripped_line}')
    
    if stripped_line.startswith("- Encrypted Character:"):
        char_value = stripped_line.split(":")[-1].strip()
        print(f'extracted char value: {char_value}')
        return(char_value)
    return None

def extract_hex(line):
    # Strip the line and extract the hex values after the "key" and "encrypted secret" lines
    stripped_line2 = line.strip()
    
    # Debugging: print the full line to see what we're receiving
    print(f"Received line: {stripped_line2}")

    # Ensure the line contains a valid hex value (after '0x')
    if stripped_line2.startswith("- XOR Key:"):
        # Extract the hex value by splitting and taking the last part
        hex_value = stripped_line2.split(":")[-1].strip()  # Returns a string like '0x42' or '0x85'
        print(f"Extracted hex value: {hex_value}")  # Debugging print
        return hex_value
    return None

for _ in range(10):
    challenge_line = p.recvline().decode().strip()
    print(challenge_line)

    while not challenge_line.startswith("- Encrypted Character:"):
        challenge_line = p.recvline().decode().strip()
        print(f'Skipping Line: {challenge_line}')

    char_line = challenge_line
    xor_key_line = p.recvline().decode().strip()

    print(f'character line: {char_line}')
    print(f'XOR key line: {xor_key_line}')

    challenge_key = extract_char(char_line)
    xor_key_hex = extract_hex(xor_key_line)

    if challenge_key is None or xor_key_hex is None:
        print('one of the values are None. Exiting...')
        break

    try:
        char_val_tohex = hex(ord(challenge_key))
        char_value = int(char_val_tohex, 16)
        xor_key_value = int(xor_key_hex, 16)
    except ValueError as e:
        print(f'err converting hexes into int: {e}')
        break
    
    answer = char_value ^ xor_key_value
    fanswer = chr(answer)
    print(answer)

    p.recvuntil('? ')
    p.sendline(fanswer)

    print(p.recvline().decode().strip())

print('retrieving the flag...')
while True:
    try:
        flag_output = p.recvline().decode().strip()
        print(flag_output)
    except EOFError:
        print('[!] Process terminated. No more data to read.')
        break

p.close()
