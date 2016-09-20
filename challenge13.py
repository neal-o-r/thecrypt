import challenge11 as c11
import challenge9  as c9
from Crypto.Random.random import getrandbits
from Crypto.Cipher import AES
import challenge6 as c6

key = bytes(getrandbits(8) for i in range(16))

def keqv_parse(input_string):

        bits = input_string.split('&')

        dict_obj = {}
        for bit in bits:
                referent = bit.split('=')[0]
                referrer = bit.split('=')[1]

                dict_obj[referent] = referrer

        return dict_obj


def decon_struct(dict_obj):

        as_string = "&".join([key + "=" + str(dict_obj[key]) \
                             for key in ["email", "uid", "role"]])

        return as_string


def profile_for(email):

        email = email.split('&')[0].split('=')[0]
        
        assert '@' and '.' in email, "this isn't an email address"

        profile = {"email": email, "uid": 10, "role": "user"}

        return decon_struct(profile)


def oracle(email):

        profile = profile_for(email)
        padded = c9.PKCS7(bytes(profile, 'ascii'), len(key))
        
        return c11.ECB_encrypt(padded, key)


def decrypt(cyphertext):

        cypher = AES.new(key, AES.MODE_ECB)
        profile = c9.unPKCS7(cypher.decrypt(cyphertext))

        return profile.decode()


def make_fake_cookie():


        fake_email = 'AAAA@AAAA.AAA'
       
        admin_block = c9.PKCS7(b'admin', 16).decode() 
        cypher_cookie = oracle(fake_email[:-3] + admin_block + fake_email[-3:])
        
        print(decrypt(cypher_cookie))

        elements = c6.chunks(cypher_cookie, 16)

        fake_cookie = elements[0] + elements[2] + elements[1]# + elements[3]
        
        return decrypt(fake_cookie)
        

if __name__ == '__main__':

        fake = make_fake_cookie()
        
        print(fake)

