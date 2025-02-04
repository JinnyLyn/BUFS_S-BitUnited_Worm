try:
    while True:
        char = input('Enter a char: ').strip()
        hex_value = input('enter a hex value: ').strip()

        try:
            hex_int = int(hex_value, 16)
        except ValueError:
            print('err: invalid hex format.')
            continue

        result = chr(ord(char) ^ hex_int)

        print(f'XOR result: {result}\n')

except KeyboardInterrupt:
    print('\n[!] Exiting.. Goodbye!')
