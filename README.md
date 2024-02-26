# StreamCrypt

StreamCrypt is a lightweight, Python-based stream cipher encryption tool designed for educational purposes and simple encryption tasks. It utilizes SHA-256 for hashing and a unique keystream generation method to encrypt and decrypt data efficiently. StreamCrypt showcases a novel approach to keystream generation that combines cryptographic best practices with performance considerations.

## Features

- **SHA-256 Hashing:** Leverages the cryptographic strength of SHA-256 for secure keystream generation.
- **Unique Salt Generation:** Uses a combination of a randomly generated salt and the current Unix timestamp to ensure that each encryption operation is unique.
- **Efficient Keystream Generation:** Implements a custom method for generating a keystream that balances cryptographic security with computational efficiency.
- **Numpy-based XOR Operations:** Utilizes Numpy for fast and efficient bitwise operations, enhancing the tool's performance for large datasets.

## Getting Started

### Prerequisites

- Python 3.6 or above
- Numpy library

### Installation

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/StreamCrypt.git
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