import base64

def convert(input_hex):

	return base64.b64encode(bytes.fromhex(input_binary))


if __name__ == '__main__':

	with open('1_hex.txt', 'r') as f:
		input_hex = f.read().strip()

	print(convert(input_hex))
