# StreamCrypt

StreamCrypt is a lightweight, Python-based stream cipher encryption tool designed for educational purposes and simple encryption tasks. It utilizes BLAKE3 for hashing and keystream generation to encrypt and decrypt data efficiently. StreamCrypt showcases a novel approach to keystream generation that combines cryptographic best practices with performance considerations.

## Features

- **BLAKE3 Hashing:** Leverages the cryptographic strength of BLAKE3.
- **Salting:** Uses a randomly generated salt to ensure that each encryption operation is unique.
- **Efficient Keystream Generation:** Balances cryptographic security with computational efficiency by using the key derivation feature of BLAKE3.
- **Numpy-based XOR Operations:** Utilizes Numpy for efficient bitwise operations, enhancing the tool's performance for large datasets.

## Getting Started

### Prerequisites

- Python 3.6 or above
- Numpy library
- blake3 library

### Installation

Clone the repository to your local machine:

```
git clone https://github.com/afkaf/StreamCrypt-Stream-Cipher.git
```

Navigate to the project directory:

```
cd StreamCrypt
```

### Usage

To use StreamCrypt for encrypting and decrypting data, follow the examples below:

```python
from streamcrypt import encrypt, decrypt

# Your secret keyword
keyword = b'your_secret_password'

# Data to encrypt (as bytes)
data_to_encrypt = b'Hello, StreamCrypt!'

# Encrypt data
encrypted_data = encrypt(keyword, data_to_encrypt)

# Decrypt data
decrypted_data = decrypt(keyword, encrypted_data)

# Verify decryption
assert data_to_encrypt == decrypted_data, "Decryption failed"
print("Decryption successful!")
```

## Project Structure

- `streamcrypt.py`: Contains the main encryption and decryption logic along with utility functions for hashing and keystream generation.

## Disclaimer

StreamCrypt is designed for educational purposes and simple encryption tasks. It has not been extensively vetted for cryptographic security. For critical applications requiring high-security encryption, please use established cryptographic libraries and standards.
