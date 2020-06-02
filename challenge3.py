from challenge2 import fixed_xor
from freq import frequency


def xor_char(x: bytes, c: bytes) -> bytes:
    return fixed_xor(x, c * len(x))


def score(string: str, frequency: dict) -> int:
    if max(string) > 127 or min(string) < 10:
        return 0

    return sum(frequency[chr(c).lower()] for c in string)


def check_all_chars(cypher: bytes, frequency: dict):

    to_byte = lambda x: bytes([x])
    scores = {
        to_byte(b): score(xor_char(cypher, to_byte(b)), frequency) for b in range(256)
    }

    return max(scores, key=scores.get), max(scores.values())


if __name__ == "__main__":

    with open("data/3.txt", "r") as f:
        cypher = bytes.fromhex(f.read().strip())

    probable_char, _ = check_all_chars(cypher, frequency)
    decyphered = xor_char(cypher, probable_char).decode("ascii")

    print(
        f"The most probable XOR character is {probable_char}and the sentence is \n{decyphered}"
    )
