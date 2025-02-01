from pwn import *

p = process(['python3', 'run.py'])


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

for _ in range 10:
    challenge_line = p.recvline().decode().strip()
    print(challenge_line)

    while not challenge_line.startswith("- Encrypted Character:"):
        challenge_line = p.recvline().decode().strip()
        print(f'Skipping Line: {challenge_line}')

        char_line = challenge_line
        xor_key_line = p.recvline().decode().strip()

        
