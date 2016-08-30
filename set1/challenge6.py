import binascii
import base64
import challenge3 as c3
import challenge5 as c5

def chunks(string, n):

        return [bytes(string[i:i + n]) for i in range(0, len(string), n)]


def hamming_dist(x, y):
        
        return sum([bin(i^j).count("1") for i,j in zip(x,y)])



def key_length(cyphertext):

        avg = []
        for i in range(2, 40):
            
                bits = chunks(cyphertext, i)
                
                h_ds = [hamming_dist(bit, bits[k-1])/float(i) for k, bit in enumerate(bits)]                
                avg.append(sum(h_ds) / float(len(h_ds)))                

        return range(2, 40)[avg.index(min(avg))]


def get_xor_key(cyphertext, key_len): 

        blocks = chunks(cyphertext, key_len)

        blocks_t = [bytes(x) for x in list(zip(*blocks[0:-1]))]

        xor_key = ''      
        for block in blocks_t:

                poss_char, _ = c3.check_all_chars(binascii.hexlify(block).decode())
                xor_key += poss_char                

        return xor_key

if __name__ == '__main__':

        with open('6_hex.txt', 'r') as f:
                cyphertext = base64.b64decode(f.read().strip())

         
        key_len = key_length(cyphertext)
        
        xor_key = get_xor_key(cyphertext, key_len)
        print("The XOR key is '%s'\n" %xor_key)
        
        cleartext = c5.padded_str_xor(cyphertext, bytes(xor_key, 'ascii'))
        print("And the cleartext is: \n", cleartext.decode())
