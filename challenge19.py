import challenge18 as c18
import challenge12 as c12
import challenge6 as c6
import challenge3 as c3
import challenge5 as c5
import base64
from freq import frequency



key = c12.randbytes(16)
nonce = 0
        
def check_all_chars(cypher):

	top_score = 0
	top_char  = ''

	for i in range(256):

		c = bytes([i])
                        
		xord = c5.padded_xor(cypher, c)
                
		if c3.score(frequency, xord) > top_score:
			top_char = c

	return top_char


def encrypt(plaintext):
	
	return c18.AES_CTR(plaintext, key, mode='enc')

def decrypt(cyphertexts):

	keystream = b''
	for i in range(16):
		cypher_slice = b"".join([bytes([c[i]]) for c in cyphertexts])
		keystream += check_all_chars(cypher_slice)

	return keystream

if __name__ == '__main__':

	with open('data/19.txt', 'r') as f:
		text = f.read().split('\n')[:-1]

	plaintexts = [base64.b64decode(i) for i in text]

	cyphertexts = [encrypt(p) for p in plaintexts]

	d = decrypt(cyphertexts)
