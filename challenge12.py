import base64
from Crypto.Random.random import getrandbits
import challenge11 as c11
import challenge9  as c9
import challenge6  as c6

key = bytes(getrandbits(8) for i in range(16))

def ECB_oracle(plaintext = b'', only=False):

        with open('data/12.txt', 'r') as f:
                unknown_64 = f.read().strip()

        unknown_bytes = base64.b64decode(unknown_64)
        if only: unknown_bytes = b''
         
        plaintext_padded = c9.PKCS7(plaintext + unknown_bytes, 16)
        return c11.ECB_encrypt(plaintext_padded, key)
        

def ECB_blocksize(ecb_instance):

        null_len = len(ecb_instance(b'', only=True))
        
        i, cypher_len = 0, 0
        while cypher_len <= null_len:
        
                cypher_len = len(ecb_instance(b'A'*i, only=True))
                i += 1

        return i-1


def get_byte_dict(oracle, n):

        small_block =  bytes([0]) * (n - 1)
	
        byte_dict = {}
        for i in range(256):
	
                s = oracle(small_block + bytes([i]))
                block = c6.chunks(s, n)

                byte_dict[block[0]] = bytes([i])
	        
        return byte_dict


def next_byte(oracle, n):

        small_block = bytes([0]) * (n - 1)
        
        byte_dict = get_byte_dict(oracle, n)

        enc_block = oracle(small_block)
    
        dict_match = enc_block[:n]
    
        return byte_dict[dict_match]


def break_ECB(oracle, n):

        
        return decoded 


if __name__ == '__main__':

        block_len = ECB_blocksize(ECB_oracle)

        random_bytes = bytes(getrandbits(8) for i in range(block_len))
        assert c11.its_ECB(ECB_oracle(random_bytes * 2, only=True))

        decyphered_char = next_byte(ECB_oracle, block_len)

