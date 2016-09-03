

def PKCS7(input_bytes, size):

	n_pad = size - len(input_bytes) % size
	
	padded = input_bytes + n_pad * bytes([n_pad])

	return padded

if __name__ == '__main__':

	str_to_pad = 'YELLOW SUBMARINE'
	
	print(PKCS7(bytes(str_to_pad, 'ascii'), 20))

