#https://cryptopals.com/sets/1/challenges/1
import base64


def convert_hx_b64(input_hex: str) -> bytes:
    """
    Take an input hexadecimal string and return it in base64
    """
    return base64.b64encode(bytes.fromhex(input_hex))


if __name__ == "__main__":
    with open("data/1.txt", "r") as f:
        input_hex, output_b64 = f.read().splitlines()

    assert convert_hx_b64(input_hex).decode() == output_b64
