from bitstring import BitArray
import time

space = int('1'*256,2)

def expand(n):
    parts = []
    while n:
        parts.append(n%1000)
        n = n//1000
    return (sum(parts)%10)+1

def expander(n):
    old = n
    while old <= space**2:
        n = expand(old)
        old = n+old*(10+n)
    return old%space

def hasher(bytestr = b''):
    if bytestr == b'':
        print('Empty bytes string')
        return
    bits = bytes_to_bits(bytestr)
    integer = int(bits,2)%space
    return hex(expander(integer))[2:].rjust(64,'0')

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def bytes_to_bits(file):
    bits = BitArray(file, endian='little').bin
    return bits

def bits_to_bytes(bits):
    bytestr = BitArray(bin=bits).tobytes()
    return bytestr

def key_hash(keyword):
    rawkey = hasher(bytes(keyword,'utf8'))
    return numberToBase(int(rawkey, 16), 256)

def time_key():
    t = time.time_ns() % 804356
    et = numberToBase(t,93)
    return ''.join([chr(i+33) for i in et])

def encrypt(keyword, text, t = 0):
    tkey = ''
    if t:
        tkey = time_key()
    key = key_hash(keyword+tkey)
    secret = []
    for i, c in enumerate(text):
        l = key[i%len(key)]
        ic, il = int(c,2), l
        secret.append(bin((il+ic)%256)[2:].rjust(8,'0'))
        if i % len(key) == 0:
            key = key_hash(''.join([bin(c)[2:].rjust(8,'0') for c in key]))
    if tkey != '':
        return secret, tkey
    return secret

def decrypt(keyword, secret, tkey = ''):
    key = key_hash(keyword+tkey)
    data = []
    for i, c in enumerate(secret):
        l = key[i%len(key)]
        ic, il = 256-int(c,2), 256-l
        data.append(bin((il-ic)%256)[2:].rjust(8,'0'))
        if i % len(key) == 0:
            key = key_hash(''.join([bin(c)[2:].rjust(8,'0') for c in key]))
    return data


with open('test.png', 'rb') as f:
    bits = bytes_to_bits(f.read())
data = []
for i, _ in enumerate(bits):
    if i % 8 == 0:
        data.append(bits[i:i+8])

keyword = 'password'

print('Data:\t',''.join(data[:24]))
print(F'Pass:\t {keyword}')
secret, tkey = encrypt(keyword, data, True)
print(f'Tkey:\t {tkey}')
print('Secret:\t',''.join(secret[:24]))

out = decrypt(keyword, secret, tkey)

print('Decrypted:\t',data == out)

# next try 2 bits, then 4 bits, then finish with 8 bits.