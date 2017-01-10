import challenge12 as c12
import challenge11 as c11
import challenge9  as c9
import challenge10 as c10
import challenge15 as c15
import base64
import random as rd


key = c12.randbytes(16)
iv  = c12.randbytes(16)

with open('data/17.txt', 'r') as f:
        text = f.read().split('\n')

plaintext = base64.b64decode(rd.choice(text[:-1]))
plaintext = bytes(range(40))

def encrypt(plaintext):

        plaintext = c9.PKCS7(2 * bytes(plaintext), len(key))

        return c11.CBC_encrypt(plaintext, key, iv)


def padding_oracle(cyphertext):

        plaintext = c10.CBC_decrypt(cyphertext, key, iv)
        
        return c15.is_PKCS7(plaintext)


def break_CBC(cyphertext, oracle, n):

        c1 = bytes([0] * (2*n - 1))
        c2 = cyphertext[:2*n]
        

        for i in range(256):            

                if padding_oracle(c2 + c1 + bytes([i])):
                         c1_byte = bytearray([i])

        inter_byte = bytearray(c1_byte[0] ^ 1)
        plain_byte = bytes(bytearray(cyphertext)[-1] ^ inter_byte[0])
        print(plain_byte.decode())

if __name__ == '__main__':

        n = len(key)

        cyphertext = encrypt(plaintext)
        
        decyphered = break_CBC(cyphertext, padding_oracle, n)

 
