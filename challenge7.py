import base64
from Crypto.Cipher import AES

if __name__ == '__main__':

        with open('data/7.txt') as f:
                cyphertext = base64.b64decode(f.read().strip())
                
        key = bytes("YELLOW SUBMARINE", 'ascii') 
        aes = AES.new(key, AES.MODE_ECB)
        
        cleartext = aes.decrypt(cyphertext)
        print(cleartext.decode())
