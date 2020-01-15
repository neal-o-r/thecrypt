from challenge3 import check_all_chars, xor_char
from freq import frequency

if __name__ == "__main__":

    with open("data/4.txt", "r") as f:
        input_hex = f.read().splitlines()

    scores = [check_all_chars(bytes.fromhex(i), frequency) for i in input_hex]

