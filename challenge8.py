from challenge6 import chunks
import binascii


def count_duplicates(cyphertext: bytes, blocksize: int) -> int:

    ctext_arr = chunks(cyphertext, blocksize)
    dupes = len(ctext_arr) - len(set(ctext_arr))
    return dupes


if __name__ == "__main__":

    with open("data/8.txt", "r") as f:
        cyphertexts = f.read().splitlines()

    cyphertexts = [bytes.fromhex(i) for i in cyphertexts]
    blocksize = 16

    cypher = max(cyphertexts, key=lambda x: count_duplicates(x, blocksize))

    print(
        "Cypher-text has likely been ECB enrcypted \n",
        binascii.hexlify(cypher).decode(),
    )
