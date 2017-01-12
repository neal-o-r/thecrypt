import challenge12 as c12
import challenge11 as c11
import challenge9  as c9
import challenge6  as c6
import challenge10 as c10
import challenge15 as c15
import base64
import random as rd


key = c12.randbytes(16)
iv  = c12.randbytes(16)

with open('data/17.txt', 'r') as f:
        text = f.read().split('\n')

#plaintext = base64.b64decode(rd.choice(text[:-1]))
plaintext = bytes(range(40))

def encrypt(plaintext):

        plaintext = c9.PKCS7(bytes(plaintext), len(key))
        
        return c11.CBC_encrypt(plaintext, key, iv)


def padding_oracle(cyphertext):

        plaintext = c10.CBC_decrypt(cyphertext, key, iv)
        
        return c15.is_PKCS7(plaintext)


def break_byte(block, prev_block, known, n_byte, n):

        c1_pre = bytes([0] * (n_byte - 1))
        
        pad_byte = (n - n_byte) + 1
        
        c1_post = []
        for i, k in enumerate(known):
                c1_post.append(k  ^ (len(known) + 1))
        
        
        c1_post = bytes(c1_post)        
         
        for i in range(256):            

                c1_dash = c1_pre + bytes([i]) + c1_post
                
                if padding_oracle(c1_dash + block):
                        found_byte = i

        plain_byte = bytes([prev_block[n_byte-1] ^ pad_byte ^ found_byte])
        return plain_byte, found_byte



def break_CBC(cyphertext, oracle, n):

        blocks = c6.chunks(cyphertext, 16)

        c1 = blocks[0]
        c2 = blocks[1]

        known = []
        found = []
        for i in range(1):
                p, f = break_byte(c2, c1, found, n-i, n)
                known.append(p)
                found.append(f)

        return known, found      
        

if __name__ == '__main__':

        n = len(key)

        cyphertext = encrypt(plaintext)
        
        decyphered, found = break_CBC(cyphertext, padding_oracle, n)
        #print(decyphered == bytes([plaintext[2*n-1]])) 
 
