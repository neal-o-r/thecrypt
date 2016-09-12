import challenge6 as c6
import binascii

def duplicate_blocks(cyphertext, blocksize):
        
        duplicates = []
        for ctext in cyphertext:

                ctext_arr = c6.chunks(ctext, blocksize)

                dup = 0
                for i, block in enumerate(ctext_arr):
                        if block in ctext_arr[:i] + ctext_arr[i+1:]:
                                dup += 1         
        
                duplicates.append(dup)

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
