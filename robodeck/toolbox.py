
def gera_pacote(pid, ref, src, dst, sid, act, len, resp):
    pac = [pid, ref, src, dst, sid, act, len, resp]
    return pac

def session_open(nome):
    nome = encode(nome)
    resp = [chr(1), chr(1), nome]
    tam = len(resp[:2]) + len(nome)
    return [resp, tam]

def encode(text):
    """Convert a string to Hex"""
    encoded = list(text)
    for n, l in enumerate(encoded):
        encoded[n] = chr(ord(l))
    # encoded = binascii.hexlify(bytes(text, "utf-8"))
    # encoded = str(encoded).strip("b")
    # encoded = encoded.strip("'")
    return encoded
