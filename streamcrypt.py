import blake3
import secrets
import numpy as np

CONTEXT = 'StreamCrypt-2db12ea77123cf47d288753b12914f61102d92a8b3a2d220c65e80a99004f3a7-by-afkaf'

def encrypt(data, keyword):
    salt = secrets.token_bytes(64)  # salt generation
    initial_key = blake3.blake3(keyword + salt, derive_key_context=CONTEXT).digest(length=64)  # Hash password and salt
    keystream = blake3.blake3(initial_key, derive_key_context=CONTEXT).digest(length=len(data))
    data_array = np.frombuffer(data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    secret = np.bitwise_xor(data_array, keystream_array).tobytes()
    return salt + secret  # Prepend salt to secret for decryption

def decrypt(secret, keyword):
    salt, encrypted_data = secret[:64], secret[64:]  # Extract salt and encrypted data
    initial_key = blake3.blake3(keyword + salt, derive_key_context=CONTEXT).digest(length=64)  # Recreate initial key
    keystream = blake3.blake3(initial_key, derive_key_context=CONTEXT).digest(length=len(encrypted_data))
    encrypted_array = np.frombuffer(encrypted_data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    data = np.bitwise_xor(encrypted_array, keystream_array).tobytes()
    return data