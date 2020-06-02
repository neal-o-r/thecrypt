from challenge2 import fixed_xor


def padded_xor(s1: bytes, s2: bytes) -> bytes:
    s2_padded = s2 * len(s1)
    return fixed_xor(s1, s2_padded)


if __name__ == "__main__":
    with open("data/5.txt", "r") as f:
        input_bytes = bytes(f.read().rstrip(), "ascii")

    xor_key = bytes("ICE", "ascii")

    binary = padded_xor(input_bytes, xor_key)
    print(binary.hex())
