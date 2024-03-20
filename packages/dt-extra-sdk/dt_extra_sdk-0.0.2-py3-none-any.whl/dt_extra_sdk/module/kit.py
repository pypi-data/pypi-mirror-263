from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(key_str: str, plaintext: str) -> bytes:
    key = key_str.encode("utf-8")[:16]
    data = pad(plaintext.encode("utf-8"), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=key[::-1])
    return cipher.encrypt(data)


def decrypt(key_str: str, ciphertext: bytes) -> str:
    key = key_str.encode("utf-8")[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv=key[::-1])
    raw_data = cipher.decrypt(ciphertext)
    data = unpad(raw_data, AES.block_size)
    return data.decode("utf-8")
