# app/security.py
import hashlib
import hmac
import os

# Generate a new salt for each password
def hash_password(password: str, salt: bytes = None) -> tuple[str, bytes]:
    if salt is None:
        salt = os.urandom(16)  # 16-byte salt
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return hashed.hex(), salt

# Verify a password
def verify_password(password: str, hashed: str, salt: bytes) -> bool:
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return hmac.compare_digest(new_hash.hex(), hashed)
