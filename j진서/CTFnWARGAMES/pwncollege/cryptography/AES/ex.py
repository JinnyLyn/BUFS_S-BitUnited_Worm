import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

aes_b64 = input('AES Key (b64): ').strip()
ct_b64 = input('Flag Ciphertext (b64): ').strip()

key = base64.b64decode(aes_b64)
ciphertext = base64.b64decode(ct_b64)

cipher = AES.new(key=key, mode=AES.MODE_ECB)
plaintext_padded = cipher.decrypt(ciphertext)

flag = unpad(plaintext_padded, AES.block_size)

print(f'FLAG: {flag.decode(errors='ignore')}')
