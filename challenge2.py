def fixed_xor(x: bytes, y: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(x, y))


if __name__ == "__main__":

    with open("data/2.txt", "r") as f:
        input_hex = f.read().splitlines()

    x = bytes.fromhex(input_hex[0])
    y = bytes.fromhex(input_hex[1])

    z = input_hex[2]

    xy = fixed_xor(x, y)
    assert xy.hex() == z
