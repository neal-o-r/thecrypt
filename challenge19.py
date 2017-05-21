import challenge18 as c18
import challenge3 as c3
import challenge12 as c12
import challenge2 as c2
import base64
from freq import frequency

key = c12.randbytes(16)
nonce = 0
        

def encrypt(plaintext):
	
	return c18.AES_CTR(plaintext, key, mode='dec')

def transpose_cyphers(cyphers):

	max_len = max(map(len, cyphers))

	c_t = [[c[i] for c in cyphers if len(c) > i] for i in range(max_len)]
	return c_t


def get_keystream(cyphers):


	cypher_t = transpose_cyphers(cyphers)
	keystream = b"".join([c3.check_all_chars(x)[0] for x in cypher_t])

	return keystream



if __name__ == '__main__':

	with open('data/19.txt', 'r') as f:
		text = f.read().split('\n')[:-1]

	plaintexts = [base64.b64decode(i) for i in text]

	cyphertexts = [encrypt(p) for p in plaintexts]
	keystream = get_keystream(cyphertexts)

	decyphered = [c2.fixed_xor(c, keystream) for c in cyphertexts]

