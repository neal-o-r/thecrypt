from challenge2 import fixed_xor
import binascii
import base64
from freq import frequency

def xor_hx_char(s, c):

        #take a hex string, xor with an ascii char, give binary

        bin_s = bytes.fromhex(s)     
        bin_c = bytes(c, 'ascii')

        pad_c = bin_c*len(bin_s)
        
        xor = fixed_xor(bin_s, pad_c)

        return xor


def score(frequency, string):

        score = 0
        for c in string:
                if c < 10 or c > 128:
                        score += 0
                else:
                        if chr(c) in frequency:
                                score += frequency[chr(c).lower()]

        return score

        
def check_all_chars(cypher):

        top_score = 0
        top_char  = ''

        for i in range(0, 127):

                c = chr(i)        
                        
                xord = xor_hx_char(cypher, c)
                
                if score(frequency, xord) > top_score:
                        top_char = c
                        top_score = score(frequency, xord)

        return top_char, top_score


if __name__ == '__main__':

        with open('3_hex.txt', 'r') as f:
                cypher = f.read().strip()

        probable_char, _ = check_all_chars(cypher) 
        decyphered = xor_hx_char(cypher, probable_char).decode('ascii')

        print("The most probable XOR character is '%s'\n"%probable_char+
                'and the sentence is \n %s' %decyphered)
 
