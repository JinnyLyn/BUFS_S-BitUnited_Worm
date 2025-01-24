from pwn import *

# Start the process with the required interpreter
p = process(['python3', 'run.py'])

# Function to safely extract both hex values from a line
def extract_hex(line):
    # Strip the line and extract the hex values after the "key" and "encrypted secret" lines
    stripped_line = line.strip()
    
    # Debugging: print the full line to see what we're receiving
    print(f"Received line: {stripped_line}")

    # Ensure the line contains a valid hex value (after '0x')
    if stripped_line.startswith("The key:") or stripped_line.startswith("Encrypted secret:"):
        # Extract the hex value by splitting and taking the last part
        hex_value = stripped_line.split(":")[-1].strip()  # Returns a string like '0x42' or '0x85'
        print(f"Extracted hex value: {hex_value}")  # Debugging print
        return hex_value
    return None

# Solve all 10 challenges
for _ in range(10):
    # Read the first challenge line, which contains the "Challenge number" text
    challenge_line = p.recvline().decode().strip()
    print(challenge_line)  # Debug: Print challenge line for context
    
    # We need to skip lines that contain "Challenge number"
    while not challenge_line.startswith("The key:"):
        challenge_line = p.recvline().decode().strip()
        print(f"Skipping line: {challenge_line}")  # Debug: Print skipped lines
    
    # Now read the next line for "The key:" and "Encrypted secret:"
    key_line = challenge_line
    encrypted_secret_line = p.recvline().decode().strip()

    # Debugging: Print the lines we are about to process
    print(f"Key line: {key_line}")
    print(f"Encrypted secret line: {encrypted_secret_line}")

    # Extract both hex values (key and encrypted secret)
    key_hex = extract_hex(key_line)
    encrypted_secret_hex = extract_hex(encrypted_secret_line)

    # Check if the extracted hex values are valid
    if key_hex is None or encrypted_secret_hex is None:
        print("Error: One of the hex values is None. Exiting.")
        break

    # Convert hex strings to integers for XOR calculation
    try:
        key = int(key_hex, 16)  # Convert '0x42' -> 66 (as int)
        encrypted_secret = int(encrypted_secret_hex, 16)  # Convert '0x85' -> 133 (as int)
    except ValueError as e:
        print(f"Error converting hex to int: {e}")
        break

    # Perform XOR operation
    plain_secret = key ^ encrypted_secret

    # Send the XOR result back as a hex string (without '0x' prefix)
    p.recvuntil("Decrypted secret? ")
    p.sendline(hex(plain_secret).lstrip("0x"))

    # Print feedback for the current challenge
    print(p.recvline().decode().strip())

# After solving all 10 challenges, extract the flag
print("Retrieving the flag...")
flag_output = p.recvall().decode().strip()

# Print the flag
print("FLAG:", flag_output)

# Close the process
p.close()

