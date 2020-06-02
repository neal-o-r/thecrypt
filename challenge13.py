import challenge11 as c11
import challenge9 as c9
import challenge12 as c12
from Crypto.Random.random import getrandbits
from Crypto.Cipher import AES
import challenge6 as c6

key = c12.randbytes(16)


def keqv_parse(input_string: str) -> dict:
    split = lambda s: s.split("=")
    return {x: y for x, y in map(split, input_string.split("&"))}


def decon_struct(dict_obj: dict) -> str:
    return "&".join(f"{key}={val}" for key, val in dict_obj.items())


def profile_for(email: str) -> str:
    email = email.replace("&", "").replace("=", "")
    assert "@" and "." in email, "this isn't an email address"

    profile = {"email": email, "uid": 10, "role": "user"}
    return decon_struct(profile)


def oracle(email: str) -> bytes:
    profile = profile_for(email)
    padded = c9.PKCS7(bytes(profile, "ascii"), len(key))
    return c11.ECB_encrypt(padded, key)


def decrypt(cyphertext: bytes) -> str:
    cypher = AES.new(key, AES.MODE_ECB)
    profile = c9.unPKCS7(cypher.decrypt(cyphertext))
    return profile.decode()


def make_fake_cookie() -> str:
    fake_email = "AAAA@AAAA.AAA"
    admin_block = c9.PKCS7(b"admin", 16).decode()
    cypher_cookie = oracle(
        fake_email.split(".")[0] + admin_block + fake_email.split(".")[-1]
    )

    elements = c6.chunks(cypher_cookie, 16)
    fake_cookie = elements[0] + elements[2] + elements[1]
    return decrypt(fake_cookie)


if __name__ == "__main__":
    fake = make_fake_cookie()
    print(fake)
