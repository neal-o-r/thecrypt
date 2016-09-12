from .challenge2 import fixed_xor
import binascii

def padded_xor(s1, s2):
        # takes 2 binary, pads 2 to 1
        # xors returns binary
        
        s2_padded = s2*len(s1)

        return fixed_xor(s1, s2_padded)


if __name__ == '__main__':

        with open('data/5.txt', 'r') as f:
                input_file = f.read().rstrip()
        
        
        xor_key = 'ICE'
        
        binary = padded_xor(bytes(input_file, 'ascii'), 
                        bytes(xor_key, 'ascii'))

        print(binascii.hexlify(binary).decode())

