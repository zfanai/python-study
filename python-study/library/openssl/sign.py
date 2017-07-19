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

#数字签名
'''
1. 公钥和私钥是配对的， 
2. 用公钥加密的数据可以用私钥解密，用私钥加密的数据可以用公钥解密
3. 公钥需要公开， 私钥是持有人私密保管。 
数字签名，达到完整性，真实性，不可抵赖性
数字签名：拥有私钥的人才有数字签名， 数字签名只解决了完整性的问题， 没有解决加密的问题， 
数字签名是对数据的摘要进行加密后跟数据一起发送， 关键点在摘要的加密， 私钥就是个人的代表， 私钥和公钥是耦合的， 
如果私钥被盗取了，那么别人也可以伪造了。 所以数字签名是包装端对端中间的数据完整性。 但是我也可以用私钥对数据进行加密， 接收者在验证
数据摘要时，先对数据进行解密，然后再验证摘要是否正确。

摘要算法：代表性的有SHA

如果私钥没有被盗取，也就是发送者没有出问题， 但是还有另外一种欺骗接收者的办法， 就是把接受者持有的别人的公钥换掉， 然后使用与这个
公钥配对的私钥来给接收者发送数据， 接收者还以为是之前的发送者，其实发送者已经变更了。

这里就有一个无法确定公钥所有者的问题， 于是就引出证书的概念。
发送者需要去证书中心对自己的公钥进行认证， 认证中心要认证中心的私钥对认证者的公钥和相关信息进行加密。 发送者有了自己的证书， 然后发送
数据的时候，除了加密后的信息摘要， 还有认证中心颁发的数字证书。
接收者不在保管发送者的公钥， 而是用认证中心的公钥去解密数字证书的内容， 得到发送者的公钥， 然后再去检查信息摘要是否正确。 

但是感觉这只是给欺骗添加了技术难度， 理论上欺骗者如果既伪造认证中心的公钥，同时也伪造发送者的证书， 这样接收数据者还是无法识别出来。

https的大概过程：
1. 客户端发送加密通信请求
2. 服务器发送加密网页和数字证书， 如果数字证书正确，就认为数据是可信的。
3. https使用的是SSL/TLS技术来保证安全， 是socket级别的安全加密， SSL/TLS是通用的安全加密通信技术。

TLS是安全传输层协议的意思。


'''