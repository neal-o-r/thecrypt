from challenge2 import fixed_xor
import binascii
import base64
from freq import frequency
from collections import defaultdict


def xor_char(s, c):
    pad_c = c * len(s)
    xor = fixed_xor(s, pad_c)
    return xor


def score(string, frequency):
    if max(string) > 127 or min(string) < 10:
        return 0

    return sum(frequency[chr(c).lower()] for c in string)


def check_all_chars(cypher, frequency):

    char_scores = {}
    for i in range(256):

        byte_c = bytes([i])
        xord = xor_char(cypher, byte_c)
        char_scores[byte_c] = score(xord, frequency)

    return max(char_scores, key=char_scores.get)


if __name__ == "__main__":

    with open("data/3.txt", "r") as f:
        cypher = bytes.fromhex(f.read().strip())

    frequency = defaultdict(int, frequency)

    probable_char = check_all_chars(cypher, frequency)
    decyphered = xor_char(cypher, probable_char).decode("ascii")

    print(
        "The most probable XOR character is '%s'\n" % probable_char
        + "and the sentence is \n %s" % decyphered
    )
