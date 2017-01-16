import base64
from challenge3 import check_all_chars
from challenge5 import padded_xor


def chunks(string, n):

        return [bytes(string[i:i + n]) for i in range(0, len(string), n)]


def hamming_dist(x, y):
        
        return sum([bin(i^j).count("1") for i, j in zip(x, y)])


def key_length(cyphertext):

        avg = []
        for i in range(2, 40):
            
                bits = chunks(cyphertext, i)
                
                h_ds = [hamming_dist(bit, bits[k-1])/float(i) for k, bit in enumerate(bits)]                
                avg.append(sum(h_ds) / float(len(h_ds)))                

        return range(2, 40)[avg.index(min(avg))]


def get_xor_key(cyphertext, key_len): 

        blocks = chunks(cyphertext, key_len)

        blocks_t = [bytes(x) for x in list(zip(*blocks[:-1]))]

        xor_key = b''      
        for block in blocks_t:

                poss_char, _ = check_all_chars(block)
                xor_key += poss_char                

        return xor_key

if __name__ == '__main__':

        with open('data/6.txt', 'r') as f:
                cyphertext = base64.b64decode(f.read().strip())

         
        key_len = key_length(cyphertext)
        
        xor_key = get_xor_key(cyphertext, key_len)
        print("The XOR key is '%s'\n" %xor_key)
        
        cleartext = padded_xor(cyphertext, xor_key)
        print("And the cleartext is: \n\n", cleartext.decode())
