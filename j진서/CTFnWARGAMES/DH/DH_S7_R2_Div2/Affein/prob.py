import random

class Affine:
    def __init__(self, key1, key2):
        assert isinstance(key1, int) and 1 <= key1 <= 250
        assert isinstance(key2, int) and 1 <= key2 <= 250
        self._key1 = key1
        self._key2 = key2

    def encrypt(self, msg):
        msg_enc = b""
        for b in msg:
            msg_enc = msg_enc + bytes([(self._key1 * b + self._key2) % 251])
        return msg_enc

    def decrypt(self, msg):
        msg_dec = b""
        for b in msg:
            msg_dec = msg_dec + bytes([pow(self._key1, -1, 251) * (b - self._key2) % 251])
        return msg_dec

def main():
    key1, key2 = random.randint(1, 250), random.randint(1, 250)
    with open("secret", "rb") as f:
        secret = f.read()
    assert b'cryptography' in secret
    
    cipher = Affine(key1, key2)
    secret_enc = cipher.encrypt(secret)
    
    print("Affine cipher? It's quite fine :>")
    print("No one can leak my secret sentence!")
    print(f"my encrypted sentence > {secret_enc.hex()}")

if __name__ == '__main__':
    main()