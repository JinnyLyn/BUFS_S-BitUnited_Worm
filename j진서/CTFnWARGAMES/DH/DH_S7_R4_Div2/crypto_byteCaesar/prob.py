import random

class Caesar:
    def __init__(self, key):
        assert isinstance(key, int) and 1 <= key <= 255
        self._key = key

    def encrypt(self, msg):
        msg_enc = b""
        for b in msg:
            msg_enc = msg_enc + bytes([(b + self._key) % 256])
        return msg_enc

    def decrypt(self, msg):
        msg_dec = b""
        for b in msg:
            msg_dec = msg_dec + bytes([(b - self._key) % 256])
        return msg_dec

def main():
    key = random.randint(1, 255)
    with open("secret", "rb") as f:
        secret = f.read()

    cipher = Caesar(key)
    secret_enc = cipher.encrypt(secret)
    print("I believe Caesar cipher is greatest encryption of all time.")
    print("No one can leak my secret sentence!")
    print(f"my encrypted sentence > {secret_enc.hex()}")

if __name__ == "__main__":
    main()