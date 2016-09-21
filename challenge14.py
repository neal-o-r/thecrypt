import base64
from Crypto.Random.random import getrandbits, randint
import challenge11 as c11
import challenge9  as c9
import challenge12 as c12
import challenge6  as c6
from tqdm import tqdm

key = bytes(getrandbits(8) for i in range(16))
pre = bytes(getrandbits(8) for i in range(randint(1, 16)))

def ECB_oracle(plaintext = b''):

        with open('data/12.txt', 'r') as f:
                unknown_64 = f.read().strip()

        unknown_bytes = base64.b64decode(unknown_64)
         
        plaintext_padded = c9.PKCS7(pre + plaintext + unknown_bytes, 16)
        return c11.ECB_encrypt(plaintext_padded, key)


def has_eq_blocks(blocks):

        for i in range(len(blocks) - 1):

                if blocks[i] == blocks[i+1]:
                        return True

        return False

def prefix_len(oracle, n):

        m, i = 0, 0
        while m == 0:

                pad_block = bytes([0] * (2 * n + i))
                enc = oracle(pad_block)

                blocks = c6.chunks(enc, n)
                
                if has_eq_blocks(blocks):
                        m = n - i
                
                i += 1

        return m


def get_byte_dict(block, oracle, n, pre_len):

        byte_dict = {}
        pad = bytes([0] * (n - pre_len))
        for i in range(256):
        
                s = oracle(pad + block + bytes([i]))
                parts = c6.chunks(s, n)
                
                byte_dict[parts[1]] = bytes([i])
                
        return byte_dict


def next_byte(block, known, oracle, n, pre_len):       
 
        byte_dict = get_byte_dict(block, oracle, n, pre_len)

        padding = bytes([0]) * (len(oracle()) - len(known) - 1 - pre_len)         
        enc_block = oracle(padding)
        dict_match = c6.chunks(enc_block, n)[len(oracle())//n - 1]
    
        return byte_dict[dict_match] if (dict_match in byte_dict) else None


def break_ECB_prefix(oracle, n, pre_len):
        
        known = b''
        block = bytes([0]) * (n - 1)
        for i in tqdm(range(len(oracle()) - pre_len)):
                
                out_byte = next_byte(block, known, oracle, n, pre_len)
                if out_byte == None: break
                        
                block += out_byte  
                block = block[1:]

                known += out_byte 

        return known


if __name__ == '__main__':

        block_len = c12.ECB_blocksize(ECB_oracle)

        random_bytes = bytes(getrandbits(8) for i in range(block_len))
        assert c11.its_ECB(ECB_oracle(random_bytes * 4))

        pre_len = prefix_len(ECB_oracle, block_len)

        decyphered_text = break_ECB_prefix(ECB_oracle, block_len, pre_len)
        print(decyphered_text.decode())


