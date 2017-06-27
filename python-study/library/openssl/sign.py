#encoding:gbk

from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign  
import base64  
   
key = load_privatekey(FILETYPE_PEM, open("private.pem").read())  
content = 'test_message' 
print key,type(key)   
d =  sign(key, content, 'sha1')  #dΪ����SHA1�㷨����ժҪ��ʹ��˽Կ����ǩ��֮�������   
print type(d), len(d)
#print d
b = base64.b64encode(d)  #��dת��ΪBASE64�ĸ�ʽ   
print b