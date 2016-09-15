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


def get_byte_dict(oracle, n):

	small_block = b'A' * (n - 1)
	
	byte_dict = {}
	for i in range(127):
		
		enc_bytes = oracle(small_block + bytes([i]))
		byte_dict[enc_bytes[:n]] = bytes([i])
		
	return byte_dict


def break_ECB(text, oracle, n):

	byte_dict = get_byte_dict(oracle, n)

	decoded = b''
	for i in text:	
		
		t = oracle(b'A' * (n-1) + bytes(i, 'ascii'))[:n]

		decoded += byte_dict[t]
	
	return decoded

if __name__ == '__main__':

        with open('data/12.txt', 'r') as f:
                unknown_64 = f.read().strip()

        with open('data/vanilla.txt', 'r') as f:
                your_string = f.read().strip()

        your_string = bytes(your_string, 'ascii')
        unknown_string = base64.b64decode(unknown_64)
        
        text = your_string + unknown_string

        block_len = ECB_blocksize(ECB_oracle)

        assert c11.its_ECB(ECB_oracle(text*2)), "it's not ECB"

        decyphered_text = break_ECB(unknown_64, ECB_oracle, block_len)

        print(base64.b64decode(decyphered_text).decode())
