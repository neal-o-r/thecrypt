import challenge9 as c9


def is_PKCS7(input_bytes):

	pad = input_bytes[-1]

	
	assert pad * bytes([pad]) == input_bytes[-pad:], 'Not PKCS7'
	return input_bytes[:pad]

if __name__ == '__main__':

	passing = c9.PKCS7(bytes('ICE ICE BABY', 'ascii'), 16)
	failing = passing[:-1] + bytes([2])	

	is_PKCS7(passing)
	is_PKCS7(failing)

