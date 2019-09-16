import base64


def convert_hx_b64(input_hex):
    return base64.b64encode(bytes.fromhex(input_hex))


if __name__ == "__main__":
    with open("data/1.txt", "r") as f:
        input_hex = f.read().splitlines()

    assert convert_hx_b64(input_hex[0]).decode() == input_hex[1]
