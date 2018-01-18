import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from crypto.fileoperations import myfile  # internal function


def generate_key_pair():
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)  # generate pub and priv key
    publickey = key.publickey().exportKey('PEM')  # pub key export for exchange
    privatekey = key.exportKey('PEM')
    myfile.writefile("testSecret.key", privatekey.decode("utf-8"))
    myfile.writefile("testPublic.key", publickey.decode("utf-8"))
    print('public key: \n{0}'.format(publickey.decode("utf-8")))


def encrypt_and_write(message, keyname, write_to):

    public_key = myfile.readfile(keyname)
    RSA_key = RSA.importKey(public_key)
    unicode_string = message.encode('utf-8', "strict")
    encrypted = RSA_key.encrypt(unicode_string, 32)
    myfile.writefile(write_to, str(encrypted))

# def decrypt_and_write(message_path, keyname, write_to):
#     public_key = myfile.readfile(keyname)
#     RSA_key = RSA.importKey(public_key)
#     encrypted = myfile.readfile(message_path)
#     decrypted = RSA_key.decrypt(encrypted)
#     myfile.writefile(write_to, str(decrypted))

# def decode_rsa(message_path, keyname):
#     public_key = myfile.readfile(keyname)
#     RSA_key = RSA.importKey(public_key)
#     cipher = PKCS1_OAEP.new(RSA_key)
#     encrypted = myfile.readfile(message_path)
#     message = cipher.decrypt(bytearray.fromhex(encrypted))
#     print(message)