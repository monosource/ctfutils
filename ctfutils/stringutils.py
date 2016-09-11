def chunks(l,n):
    """Yield n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

def strxor(s1, s2, out='string'):
    """XOR two strings together
    """
    xored = [chr(ord(x1) ^ ord(x2)) for (x1, x2) in zip(s1, s2)]
    if out == 'string':
        return ''.join(xored)
    elif out == 'list':
        return xored

def bindecode(s, out='string'):
    """Decode string of bits.
    """
    sbytes = list(chunks(s,8))
    dec = map(lambda x: chr(int(x, 2)), sbytes)
    if out == 'string':
        return ''.join(dec)
    elif out == 'list':
        return dec

def binencode(s, out='string'):
    """Encode as string of bits
    """
    enc = map(lambda x: bin(ord(x))[2:].rjust(8, '0'), s)
    if out == 'string':
        return ''.join(enc)
    elif out == 'list':
        return enc
