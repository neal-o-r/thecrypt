import base64
from Crypto.Random.random import getrandbits, randint
import challenge11 as c11
import challenge9 as c9
import challenge12 as c12
import challenge6 as c6


key = c12.randbytes(16)
pre = c12.randbytes(randint(1, 16))


def ECB_oracle(plaintext: bytes = b"") -> bytes:
    with open("data/12.txt", "r") as f:
        unknown_64 = f.read().strip()

    unknown_bytes = base64.b64decode(unknown_64)
    plaintext_padded = c9.PKCS7(pre + plaintext + unknown_bytes, 16)
    return c11.ECB_encrypt(plaintext_padded, key)


def has_eq_blocks(blocks: list) -> bool:
    return any(ah == be for be, ah in zip(blocks, blocks[1:]))


def prefix_len(oracle: callable, n: int) -> int:
    i = 0
    while True:
        pad_block = bytes([0] * (2 * n + i))
        enc = oracle(pad_block)
        blocks = c6.chunks(enc, n)
        if has_eq_blocks(blocks):
            return n - i
        else:
            i += 1


def get_byte_dict(block: bytes, oracle: callable, n: int, pre_len: int) -> dict:
    pad = bytes([0] * (n - pre_len))
    byt = [bytes([i]) for i in range(256)]

    bdict = {c6.chunks(oracle(pad + block + b), n)[1]: b for b in byt}
    return bdict


def next_byte(
    block: bytes, known: bytes, oracle: callable, n: int, pre_len: int
) -> bytes:

    byte_dict = get_byte_dict(block, oracle, n, pre_len)

    padding = bytes([0]) * (len(oracle()) - len(known) - pre_len - 1)
    enc_block = oracle(padding)
    dict_match = c6.chunks(enc_block, n)[len(oracle()) // n - 1]

    return byte_dict[dict_match] if (dict_match in byte_dict) else None


def break_ECB_prefix(oracle: callable, n: int, pre_len: int) -> bytes:

    cat = lambda b: b"".join(b)

    out_bytes = []
    block = bytes([0] * (n - 1))
    o = next_byte(block, cat(out_bytes), oracle, n, pre_len)

    while o is not None:
        block += o
        block = block[1:]
        out_bytes.append(o)

        o = next_byte(block, cat(out_bytes), oracle, n, pre_len)

    return cat(out_bytes)


if __name__ == "__main__":

    block_len = c12.ECB_blocksize(ECB_oracle)

    random_bytes = bytes(getrandbits(8) for i in range(block_len))
    assert c11.its_ECB(ECB_oracle(random_bytes * 4))

    pre_len = prefix_len(ECB_oracle, block_len)

    decyphered_text = break_ECB_prefix(ECB_oracle, block_len, pre_len)
    print(decyphered_text.decode())
