from challenge3 import check_all_chars, xor_char
from freq import frequency

if __name__ == "__main__":

    with open("data/4.txt", "r") as f:
        input_bytes = list(map(bytes.fromhex, f.read().splitlines()))

    scores = [check_all_chars(b, frequency) for b in input_bytes]

    top_score = max(scores, key=lambda x: x[1])
    i = scores.index(top_score)

    print(xor_char(input_bytes[i], top_score[0]))
