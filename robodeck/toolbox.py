import binascii

def gera_pacote(pid, ref, src, dst, sid, act, len, resp):
    pac = [pid, ref, src, dst, sid, act, len, resp]
    return pac

def session_open(nome):
    nome = encode(nome)
    resp = [b'0x81', b'0x01', nome]
    tam = len(resp)
    return [resp, tam]

def encode(text):
    """Convert a string to Hex"""
    encoded = binascii.hexlify(bytes(text, "utf-8"))
    encoded = str(encoded).strip("b")
    encoded = encoded.strip("'")
    return encoded
