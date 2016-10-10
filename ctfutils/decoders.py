def manchester(inp, op='encode'):
    """
    Encodes/decodes Manchester
    Input: string (for encode); string of bits (for decode)
    """
    pass

def manchester_diff(inp, op='encode'):
    """
    Encodes/decodes differential Manchester
    Input: string (for encode op); string of bits (for decode)
    """
    if op == 'encode':
        pass
    elif op == 'decode':
        pass
    pass


# TODO
'''
def morse(s, dash='-'):
    """Encode string as Morse code string.
    """
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    mcodes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
                '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
    d=dict(zip(alph, mcodes))
    return replace(s, d)


def morsedec(s):
    """Decode morse string.
    """
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    mcodes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
                '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
    d=dict(zip(mcodes, alph))
    return replace(s, d)
'''
