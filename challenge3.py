from challenge2 import fixed_xor
import binascii
import base64
from freq import frequency


def xor_char(s, c):

	pad_c = c*len(s)

	xor = fixed_xor(s, pad_c)

	return xor


def score(frequency, string):

	score = 0
	for c in string:
		if c > 10 and c < 127 and chr(c) in frequency:
			score += frequency[chr(c).lower()]

	return score

        
def check_all_chars(cypher):

        top_score = 0
        top_char  = ''

        for i in range(0, 127):

                byte_c = bytes([i])
                        
                xord = xor_char(cypher, byte_c)
                
                if score(frequency, xord) > top_score:
                        top_char = chr(i)
                        top_score = score(frequency, xord)

        return top_char, top_score


if __name__ == '__main__':

        with open('data/3.txt', 'r') as f:
                cypher = bytes.fromhex(f.read().strip())
	
        probable_char, _ = check_all_chars(cypher) 
        decyphered = xor_char(cypher, 
			bytes(probable_char, 'ascii')).decode('ascii')

        print("The most probable XOR character is '%s'\n"%probable_char+
                'and the sentence is \n %s' %decyphered)
