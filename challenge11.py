from Crypto.Random.random import randrange, getrandbits
from Crypto.Cipher import AES
import challenge6 as c6
import challenge2 as c2
import challenge8 as c8
import challenge9 as c9
from collections import namedtuple
from tqdm import tqdm


def ECB_encrypt(cleartext: bytes, key: bytes) -> bytes:
    cypher = AES.new(key, AES.MODE_ECB)
    cyphertext = cypher.encrypt(cleartext)
    return cyphertext


def CBC_encrypt(cleartext: bytes, key: bytes, initialization: bytes) -> bytes:
    cypher = AES.new(key, AES.MODE_ECB)
    blocks = c6.chunks(cleartext, len(key))

    vector = initialization
    cyphertext = b""
    for block in blocks:

        xor_block = c2.fixed_xor(block, vector)
        enc_block = cypher.encrypt(xor_block)
        cyphertext += enc_block
        vector = enc_block

    return cyphertext


def black_box(cleartext: bytes):

    output = namedtuple("Output", ["type", "text"])

    cleartext = bytes(randrange(5, 11)) + plaintext + bytes(randrange(5, 11))
    cleartext = c9.PKCS7(plaintext, 16)
    key = bytes(getrandbits(8) for i in range(16))

    coin_flip = randrange(0, 2)
    if coin_flip:
        return output(coin_flip, ECB_encrypt(cleartext, key))

    init_vec = bytes(getrandbits(8) for i in range(16))
    return output(coin_flip, CBC_encrypt(cleartext, key, init_vec))


def its_ECB(cyphertext: bytes, n: int = 16) -> bool:
    return c8.count_duplicates(cyphertext, n) > 0


if __name__ == "__main__":

    with open("data/vanilla.txt", "r") as f:
        plaintext = bytes(f.read(), "ascii") * 2

    right = 0
    for _ in range(100):

        jibber_jabber = black_box(plaintext)
        ECB = its_ECB(jibber_jabber.text)
        right += ECB == jibber_jabber.type

    print(f"The detection oracle got {right}% correct")
