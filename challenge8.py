from challenge6 import chunks
import binascii

def count_duplicates(cyphertext, blocksize):

	ctext_arr = chunks(cyphertext, blocksize)
	dup = len(ctext_arr) - len(set(ctext_arr))        

	return dup

def duplicate_blocks(cyphertexts, blocksize):
        
	duplicates = []
	for ctext in cyphertexts:
		duplicates.append(count_duplicates(ctext, blocksize))
        
	return duplicates


if __name__ == '__main__':

        with open('data/8.txt', 'r') as f:
                cyphertexts = f.read().splitlines()
        
        cyphertexts = [bytes.fromhex(i) for i in cyphertexts]
        
        blocksize = 16
       
        dups = duplicate_blocks(cyphertexts, blocksize)
        i = dups.index(max(dups))

        print('Cypher-text %d has likely been ECB enrcypted \n'%i,
                binascii.hexlify(cyphertexts[i]).decode()) 
