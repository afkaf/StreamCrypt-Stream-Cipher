import blake3
import secrets
import time
import numpy as np

def hasher(data):
    return blake3.blake3(data).digest()

def generate_unique_salt(length):
    salt = secrets.token_bytes(length)
    unix_time = int(time.time_ns())
    time_bytes = unix_time.to_bytes((unix_time.bit_length() + 7) // 8, 'big')
    unique_input = salt + time_bytes
    key = hasher(unique_input)
    return key

def keystream_generator(initial_key, data_length):
    keystream = bytearray()
    counter = 0
    while len(keystream) < data_length:
        counter_bytes = counter.to_bytes(8, 'big')
        keystream_part = hasher(initial_key + counter_bytes)
        keystream.extend(keystream_part)
        counter += 1
        if len(keystream) > data_length:
            keystream = keystream[:data_length]
    return bytes(keystream)

def encrypt(keyword, data):
    salt = generate_unique_salt(32)  # salt generation
    initial_key = hasher(keyword + salt)  # Combine and hash password and salt
    keystream = keystream_generator(initial_key, len(data))
    data_array = np.frombuffer(data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    secret = np.bitwise_xor(data_array, keystream_array).tobytes()
    return salt + secret  # Prepend salt to secret for decryption

def decrypt(keyword, secret):
    salt, encrypted_data = secret[:32], secret[32:]  # Extract salt and encrypted data
    initial_key = hasher(keyword + salt)  # Recreate initial key
    keystream = keystream_generator(initial_key, len(encrypted_data))
    encrypted_array = np.frombuffer(encrypted_data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    data = np.bitwise_xor(encrypted_array, keystream_array).tobytes()
    return data