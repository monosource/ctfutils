def chunks(l,n):
    """Yield n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

def strxor(s1, s2):
    """XOR two strings together
    """
    return ''.join([chr(ord(x1) ^ ord(x2)) for (x1, x2) in zip(s1,s2)])
