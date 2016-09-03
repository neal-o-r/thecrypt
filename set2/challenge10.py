import base64
from Crypto.Cipher import AES
import import_set1
import set1.challenge6 as c6
import set1.challenge2 as c2


def decrypt_AES(cyphertext, key, initialization):

	blocks = c6.chunks(cyphertext, len(key))
	aes_cypher = AES.new(key, AES.MODE_ECB)


	vec = initialization
	cleartext = b''
	for block in blocks:

		decrypt = aes_cypher.decrypt(block)
		cleartext += c2.fixed_xor(decrypt, vec)
		vec = block

	return cleartext


if __name__ == '__main__':

	with open('data/10.txt', 'r') as f:
		cyphertext = f.read().strip()

	cyphertext = base64.b64decode(cyphertext)

	key = bytes("YELLOW SUBMARINE", 'ascii')
	init_vec = bytes([0] * len(key))
	
	decrypted = decrypt_AES(cyphertext, key, init_vec)
	
	text = decrypted.decode()
	print(text)	

