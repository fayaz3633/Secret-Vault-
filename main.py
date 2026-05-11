from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class AESCipher:
    def __init__(self, key: bytes):
        self.key = key  # 32 bytes for AES-256

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(32)

    def encrypt(self, data: bytes) -> bytes:
        nonce = os.urandom(12)
        ciphertext = AESGCM(self.key).encrypt(nonce, data, None)
        return nonce + ciphertext

    def decrypt(self, encrypted: bytes) -> bytes:
        nonce = encrypted[:12]
        ciphertext = encrypted[12:]
        return AESGCM(self.key).decrypt(nonce, ciphertext, None)
