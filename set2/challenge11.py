from Crypto.Random.random import randrange, getrandbits
from Crypto.Cipher import AES
import import_set1
from set1 import challenge6 as c6
from set1 import challenge2 as c2
from set1 import challenge8 as c8
import challenge9 as c9
from collections import namedtuple
from tqdm import tqdm

def ECB_encrypt(cleartext, key):

	cypher = AES.new(key, AES.MODE_ECB)
	cyphertext = cypher.encrypt(cleartext)
	return cyphertext


def CBC_encrypt(cleartext, key, initialization):

	cypher = AES.new(key, AES.MODE_ECB)
	blocks = c6.chunks(cleartext, len(key))

	vector = initialization
	cyphertext = b''
	for block in blocks:

		xor_block = c2.fixed_xor(block, vector)
		enc_block = cypher.encrypt(xor_block)
		cyphertext += enc_block
		vector = enc_block

	return cyphertext


def black_box(cleartext):

	OUT = namedtuple('OUT', ['Type', 'Text'])
	cleartext = bytes(randrange(5, 11)) + plaintext + bytes(randrange(5, 11))
	cleartext = c9.PKCS7(plaintext, 16)
	key = bytes(getrandbits(8) for i in range(16))
	
	coin_flip = randrange(0,2)

	if coin_flip == 0:

		return OUT(coin_flip, ECB_encrypt(cleartext, key))

	if coin_flip == 1:

		init_vec = bytes(getrandbits(8) for i in range(16))			
		return OUT(coin_flip, CBC_encrypt(cleartext, key, init_vec))	
	
def its_ECB(cyphertext):

	return c8.count_duplicates(cyphertext, 16) > 0

if __name__ == '__main__':

	with open('data/vanilla.txt', 'r') as f:
		plaintext = bytes(f.read(), 'ascii')*2
	
	right = 0
	for i in tqdm(range(100)):	
	
		jibber_jabber = black_box(plaintext)
		ECB = its_ECB(jibber_jabber.Text)
		if ECB != jibber_jabber.Type: 
			right += 1

	print('The detection oracle got %d%% correct' %right)
