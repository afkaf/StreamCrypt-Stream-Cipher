import blake3
import secrets
import time
import numpy as np

def hasher(data):
    return blake3.blake3(data).digest()

def generate_unique_salt():
    salt = secrets.token_bytes(32)
    unix_time = int(time.time_ns())
    time_bytes = unix_time.to_bytes((unix_time.bit_length() + 7) // 8, 'big')
    unique_input = salt + time_bytes
    key = hasher(unique_input)
    return key

def generate_keystream(key, length):
    context = "StreamCrypt-Stream-Cipher by afkaf"
    keystream = blake3.blake3(key, derive_key_context=context).digest(length=length)
    return keystream

def encrypt(keyword, data):
    salt = generate_unique_salt()  # salt generation
    initial_key = hasher(keyword + salt)  # Combine and hash password and salt
    keystream = generate_keystream(initial_key, len(data))
    data_array = np.frombuffer(data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    secret = np.bitwise_xor(data_array, keystream_array).tobytes()
    return salt + secret  # Prepend salt to secret for decryption

def decrypt(keyword, secret):
    salt, encrypted_data = secret[:32], secret[32:]  # Extract salt and encrypted data
    initial_key = hasher(keyword + salt)  # Recreate initial key
    keystream = generate_keystream(initial_key, len(encrypted_data))
    encrypted_array = np.frombuffer(encrypted_data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    data = np.bitwise_xor(encrypted_array, keystream_array).tobytes()
    return data