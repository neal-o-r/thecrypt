import challenge18 as c18
import challenge12 as c12
import base64


key = c12.randbytes(16)
nonce = 0

def encrypt(plaintexts):
	
	cyphertexts = []
	for plaintext in plaintexts:
		cyphertexts.append(c18.AES_CTR(plaintext, key, mode='enc'))

	return cyphertexts

if __name__ == '__main__':

	with open('data/19.txt', 'r') as f:
		text = f.read().split('\n')[:-1]

	plaintexts = [base64.b64decode(i) for i in text]

	cyphertexts = encrypt(plaintexts)

