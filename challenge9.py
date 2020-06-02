def PKCS7(input_bytes: bytes, size: int) -> bytes:

    n_pad = size - len(input_bytes) % size

    return input_bytes + n_pad * bytes([n_pad])


def unPKCS7(input_bytes: bytes) -> bytes:
    return input_bytes[: (len(input_bytes) - input_bytes[-1])]


if __name__ == "__main__":

    to_pad = b"YELLOW SUBMARINE"

    print(PKCS7(to_pad, 20))
