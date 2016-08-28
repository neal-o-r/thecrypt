
def fixed_xor(x, y):

	out_bin = ''
	for i, j in zip(x,y):
	    
    		out_bin += str(int(i)^int(j))
   
	return out_bin

if __name__ == '__main__':

	with open('2_hex.txt', 'r') as f:
		input_hex = f.read().splitlines()
	
	x = bin(int(input_hex[0], 16))[2:]
	y = bin(int(input_hex[1], 16))[2:]

	print(hex(int(fixed_xor(x, y), 2)))
