import challenge19 as c19
import challenge2 as c2
import base64


if __name__ == '__main__':

        with open('data/20.txt', 'r') as f:
                text = f.read().split('\n')[:-1]

        plaintexts = [base64.b64decode(i) for i in text]

        cyphertexts = [c19.encrypt(p) for p in plaintexts]
        keystream = c19.get_keystream(cyphertexts)

        decyphered = [c2.fixed_xor(c, keystream) for c in cyphertexts]
