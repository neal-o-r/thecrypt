import challenge9  as c9
import challenge10 as c10
import challenge11 as c11
import challenge12 as c12


key = c12.randbytes(16)
iv  = c12.randbytes(16)

def CBC_encrypt_string(input_string):

        pre  = b"comment1=cooking%20MCs;userdata="
        post = b";comment2=%20like%20a%20pound%20of%20bacon"

        input_string = input_string.replace(";", "").replace("=", "")
        plaintext = c9.PKCS7(pre + bytes(input_string, "ascii") + post, len(key))

        return c11.CBC_encrypt(plaintext, key, iv)

def check(cyphertext):

        plaintext = c10.CBC_decrypt(cyphertext, key, iv)
        plaintext = plaintext.decode(errors='replace')

        return "admin=true" in plaintext


if __name__ == '__main__':

        admin = 'admin<true'
        admin_block = '0' * (2*len(key) - len(admin)) + admin
 
        
        cyphertext = CBC_encrypt_string(admin_block)
        cyphertext = bytearray(cyphertext)

        cyphertext[43] = cyphertext[43] ^ 1


        print(check(bytes(cyphertext)))
