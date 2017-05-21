import binascii


def fixed_xor(x, y):
        # takes binary, xor's, returns binary

	out_bin = bytearray()
	for i, j in zip(x, y):
	    
    		out_bin.append(i ^ j)
   
	return bytes(out_bin)


if __name__ == '__main__':

        with open('data/2.txt', 'r') as f:
                input_hex = f.read().splitlines()
	
        x = bytes.fromhex(input_hex[0])
        y = bytes.fromhex(input_hex[1])

        z = input_hex[2]

        xy_bytes = fixed_xor(x, y)
        print(binascii.hexlify(xy_bytes).decode() == z)
