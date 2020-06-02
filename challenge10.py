import base64
from Crypto.Cipher import AES
import challenge6 as c6
import challenge2 as c2


def CBC_decrypt(cyphertext: bytes, key: bytes, initialization: bytes) -> bytes:

    blocks = c6.chunks(cyphertext, len(key))
    aes_cypher = AES.new(key, AES.MODE_ECB)

    vec = initialization
    cleartext = b""
    for block in blocks:
        decrypt = aes_cypher.decrypt(block)
        cleartext += c2.fixed_xor(decrypt, vec)
        vec = block

    return cleartext


if __name__ == "__main__":

    with open("data/10.txt", "r") as f:
        cyphertext = f.read().strip()

    cyphertext = base64.b64decode(cyphertext)

    key = bytes("YELLOW SUBMARINE", "ascii")
    init_vec = bytes([0] * len(key))

    decrypted = CBC_decrypt(cyphertext, key, init_vec)

    print(decrypted.decode())
