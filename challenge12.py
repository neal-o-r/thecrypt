import base64
from Crypto.Random.random import getrandbits
import challenge11 as c11
import challenge9 as c9
import challenge6 as c6


def randbytes(n: int) -> bytes:
    return bytes(getrandbits(8) for i in range(n))


key = randbytes(16)


def ECB_oracle(plaintext: bytes = b""):
    with open("data/12.txt", "r") as f:
        unknown_64 = f.read().strip()

    unknown_bytes = base64.b64decode(unknown_64)
    plaintext_padded = c9.PKCS7(plaintext + unknown_bytes, 16)

    return c11.ECB_encrypt(plaintext_padded, key)


def ECB_blocksize(oracle: callable, block: bytes = b"A") -> int:

    null_len = len(oracle())
    cypher_len = len(oracle(block))
    if cypher_len > null_len:
        return cypher_len - null_len

    return ECB_blocksize(oracle, block + b"A")


def get_byte_dict(block: bytes, oracle: callable, n: int) -> dict:

    byte_dict = {
        c6.chunks(oracle(block + bytes([i])), n)[0]: bytes([i]) for i in range(256)
    }

    return byte_dict


def next_byte(block: bytes, known: bytes, oracle: callable, n: int) -> bytes:

    byte_dict = get_byte_dict(block, oracle, n)

    padding = bytes([0]) * (len(oracle()) - len(known) - 1)

    enc_block = oracle(padding)
    dict_match = c6.chunks(enc_block, n)[len(oracle()) // n - 1]

    return byte_dict[dict_match] if (dict_match in byte_dict) else None


def break_ECB(oracle: callable, n: int):

    known = b""
    block = bytes([0]) * (n - 1)
    for i in range(len(oracle())):

        out_byte = next_byte(block, known, oracle, n)
        if out_byte is None:
            break

        block += out_byte
        block = block[1:]

        known += out_byte

    return known


if __name__ == "__main__":

    block_len = ECB_blocksize(ECB_oracle)

    random_bytes = bytes(getrandbits(8) for i in range(block_len))
    assert c11.its_ECB(ECB_oracle(random_bytes * 4))

    decyphered_text = break_ECB(ECB_oracle, block_len)
    print(decyphered_text.decode())
