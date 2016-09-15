import base64
from Crypto.Random.random import getrandbits
import challenge11 as c11
import challenge9  as c9

key = bytes(getrandbits(8) for i in range(16))

def ECB_oracle(plaintext):

        plaintext_padded = c9.PKCS7(plaintext, 16)
        return c11.ECB_encrypt(plaintext_padded, key)
        

def ECB_blocksize(ecb_instance):

        null_len = len(ecb_instance(b''))
        
        i, cypher_len = 0, 0
        while cypher_len <= null_len:
        
                cypher_len = len(ecb_instance(b'A'*i))
                i += 1
        return i-1


def break_ECB(text, oracle):

        


if __name__ == '__main__':

        with open('data/12.txt', 'r') as f:
                unknown_string = f.read().strip()

        with open('data/vanilla.txt', 'r') as f:
                your_string = f.read().strip()

        your_string = bytes(your_string, 'ascii')
        unknown_string = base64.b64decode(unknown_string)
        
        text = your_string + unknown_string

        block_len = ECB_blocksize(ECB_oracle)

        assert c11.its_ECB(ECB_oracle(text*2)), "it's not ECB"

        decyphered_text = break_ecb(text, ECB_oracle)


