#encoding:gbk

from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign  
import base64  
   
key = load_privatekey(FILETYPE_PEM, open("private.pem").read())  
content = 'test_message' 
print key,type(key)   
d =  sign(key, content, 'sha1')  #d为经过SHA1算法进行摘要、使用私钥进行签名之后的数据   
print type(d), len(d)
#print d
b = base64.b64encode(d)  #将d转换为BASE64的格式   
print b