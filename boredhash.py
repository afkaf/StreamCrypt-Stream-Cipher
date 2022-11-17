from bitstring import BitArray

space = int('1'*256,2)

def bytes_to_bits(file):
	bits = BitArray(file, endian='little').bin
	return bits

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
