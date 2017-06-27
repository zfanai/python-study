#!/usr/bin/python
#encoding:gbk

from Crypto.PublicKey import RSA
#from Crypto.PublicKey import RSA
#from Crypto.PublicKey import RSA
#from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
#from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
#from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode
#from base64 import b64decode

def encrypt(message):
    externKey="./myPublicKey.pem"
    privatekey = open(externKey, "r")
    encryptor = RSA.importKey(privatekey, passphrase="f00bar")
    encriptedData=encryptor.encrypt(message, 0)
    file = open("./cryptThingy.txt", "wb")
    file.write(encriptedData[0])
    file.close()
    
def decrypt():
    externKey="./myPrivateKey.pem"
    publickey = open(externKey, "r")
    decryptor = RSA.importKey(publickey, passphrase="f00bar")
    retval=None
    file = open("./cryptThingy.txt", "rb")
    retval = decryptor.decrypt(file.read())
    file.close()
    return retval

#Rsa私钥签名，公钥验签的Python代码
#sign.py

def rsa_sign(message):
    private_key_file = open('./myPrivateKey.pem', 'r')
    private_key = RSA.importKey(private_key_file)
    hash_obj = SHA.new(message)
    signer = PKCS1_v1_5.new(private_key)
    d = b64encode(signer.sign(hash_obj))
    file = open('./signThing.txt', 'wb')
    file.write(d)
    file.close()

#verify.py


def rsa_verify(message):
    public_key_file = open('./myPublicKey.pem', 'r')
    public_key = RSA.importKey(public_key_file)
    sign_file = open('./signThing.txt', 'r')
    sign = b64decode(sign_file.read())
    h = SHA.new(message)
    verifier = PKCS1_v1_5.new(public_key)
    return verifier.verify(h, sign)

# 
'''
if '__main__' == __name__:
    rsa_sign('zhangshibo') 
if __name__ == "__main__":
    encryptedThingy=encrypt("Loren ipsum")    
if __name__ == "__main__":
    decryptedThingy=decrypt()
    print "Decrypted: %s" % decryptedThingy    
if '__main__' == __name__:
    print rsa_verify('zhangshibo') '''
if '__main__' == __name__:
    encryptedThingy=encrypt("Loren ipsum")    
    decryptedThingy=decrypt()
    print "Decrypted: %s" % decryptedThingy   
    rsa_sign('zhangshibo') 
    print rsa_verify('zhangshibo')    