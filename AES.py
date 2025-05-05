import sys
import ast

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#salt_gen = get_random_bytes(32)
#print(salt_gen)
#copy the generated salt in the salt variable

salt = b'F\xc6\x7f\xf4\xc0\x11\xe5b\xc6\xfa\x11/\xfeZ)\x98\xab\xa9\xca\x059\x02on\xbe\x13Dvd\x86\xd4\xb1'
password = "mysecretkeee"  #set the password of your choice
key = b'\x04\xB0\x13\xA9\xD7\xEB\x8A\x07\xB0\xCA\xEA\x2E\xA8\xD6\x2B\x82\xA8\x24\x99\x6E\x7C\x1E\x88\x4C\x29\x85\x43\x85\x81\xB7\x45\xF9'#PBKDF2(password, salt, dkLen=32)
iv = b'\x11\xA1\x33\xA7\x01\x46\x2C\x4A\xAE\xBA\x9A\xDE\x94\x5F\xEC\x6B' #put the iv of your choice but of the same size


message = input("Enter the message you want to cipher/decipher: ")
if message.startswith("b'") and message.endswith("'"):
    message = ast.literal_eval(message)  
else:
    message = message.encode()

def cipherthetext(message):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    return ciphered_data

def decipherthetext(ciphered_data, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    deciphered_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    return deciphered_data

ask = input("enter c to cypher and d for decipher: ")
ask = ask.lower()

if ask == "c":
    ciphered_data = cipherthetext(message)
    print("secret message (raw bytes):", ciphered_data)
    print("secret message (hex format):", ''.join(f'\\x{b:02X}' for b in ciphered_data))
    print("IV:", ''.join(f'\\x{b:02X}' for b in iv))


elif ask == "d":
    ciphered_data = message
    deciphered_data = decipherthetext(ciphered_data,iv)
    print("message: ", deciphered_data.decode())
