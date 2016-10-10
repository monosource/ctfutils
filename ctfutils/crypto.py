from string import punctuation, ascii_lowercase, ascii_uppercase

def word_score(inp, word_file_path='/usr/share/dict/words'):
    """
    Returns score for input string.
    """
    with open(word_file_path) as f:
        words = f.read()
    words = words.split()
    preprocessed_inp = inp.translate(None, punctuation)
    count = 0
    words_in_inp = preprocessed_inp.split(' ')
    for word in words_in_inp:
        if word in words:
            count += 1
    return count

# TODO General alphabet?
def rotn(inp, n):
    """
    Rotate by N in 26 letter alphabet, uppercase, lowercase
    """
    res = ''
    for i in inp:
        if i in ascii_lowercase:
            res += chr(((ord(i) - ord('a') + n) % 26) + ord('a'))
        elif i in ascii_uppercase:
            res += chr(((ord(i) - ord('A') + n) % 26) + ord('A'))
        else:
            res += i
    return res

def proof_of_work(prefix, alg, bits, where):
    """
    Solves proof of work
    """
    if where == 'start':
        pass
    elif where == 'end':
        pass
    pass

def counts(inp):
    """
    Returns a dict with counts for each character in the input
    """
    c = {}
    for i in inp:
        if i in f:
            c[i] += 1
        else:
            c[i] = 1
    return c

# TODO: make it work for arbitrary alphabets.
def caesar(inp, verbose=False):
    """
    Returns caesar solution as (text, shift_key)
    verbose: returns all pairs of (text, shift_key)
    """
    if not verbose:
        ws = 0
        mws = 0
        key = 0
        candidate = ''
        for i in range(26):
            temp = rotn(inp, i)
            ws = word_score(temp)
            if mws < ws:
                mws = ws
                key = i
                candidate = temp

        return candidate, key
    else:
        rots = []
        for i in range(26):
            rots.append((i, rotn(inp, i)))
        return rots

def substitute():
    pass
