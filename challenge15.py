import challenge9 as c9


def is_PKCS7(input_bytes: bytes) -> bool:
    pad = input_bytes[-1]
    if pad * bytes([pad]) == input_bytes[-pad:]:
        return True
    else:
        return False


if __name__ == "__main__":

    passing = c9.PKCS7(bytes("ICE ICE BABY", "ascii"), 16)
    failing = passing[:-1] + bytes([2])

    print(is_PKCS7(passing))
    print(is_PKCS7(failing))
