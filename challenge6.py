import base64
from typing import List
from challenge3 import check_all_chars
from challenge5 import padded_xor
from freq import frequency


def chunks(string: str, n: int) -> List[bytes]:
    return [bytes(string[i : i + n]) for i in range(0, len(string), n)]


def hamming_dist(x: bytes, y: bytes) -> int:
    return sum(bin(i ^ j).count("1") for i, j in zip(x, y))


def roll_1(lst: list) -> list:
    return lst[-1:] + lst[:-1]


def key_length(cyphertext: bytes) -> int:
    avg = []
    for i in range(2, 40):

        bits = chunks(cyphertext, i)
        h_ds = [hamming_dist(b1, b2) / i for b1, b2 in zip(bits, roll_1(bits))]

        avg.append(sum(h_ds) / len(h_ds))

    return range(2, 40)[avg.index(min(avg))]


def get_xor_key(cyphertext: bytes, key_len: int, frequency: dict) -> bytes:

    blocks = chunks(cyphertext, key_len)
    blocks_transposed = [bytes(x) for x in zip(*blocks[:-1])]

    key = b"".join(check_all_chars(b, frequency)[0] for b in blocks_transposed)

    return key


if __name__ == "__main__":
    with open("data/6.txt", "r") as f:
        cyphertext = base64.b64decode(f.read().strip())

    key_len = key_length(cyphertext)

    xor_key = get_xor_key(cyphertext, key_len, frequency)
    print(f"The XOR key is '{xor_key}'\n")

    cleartext = padded_xor(cyphertext, xor_key)
    print(f"And the cleartext is: \n\n {cleartext.decode()}")
