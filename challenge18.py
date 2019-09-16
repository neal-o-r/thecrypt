from Crypto.Cipher import AES
from struct import pack
import base64
import challenge6 as c6
import challenge2 as c2


def AES_CTR(cyphertext, key, nonce=0):

    n = len(key)

    blocks = c6.chunks(cyphertext, n)
    aes_cypher = AES.new(key, AES.MODE_ECB)

    out = b""
    ctr = 0
    for block in blocks:

        keystream = pack("<QQ", nonce, ctr)
        ctr += 1

        out += c2.fixed_xor(aes_cypher.encrypt(keystream), block)

    return out


if __name__ == "__main__":

    with open("data/18.txt", "r") as f:
        cyphertext = base64.b64decode(f.read().strip())

    key = b"YELLOW SUBMARINE"

    plaintext = AES_CTR(cyphertext, key)
