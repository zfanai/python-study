#encoding:utf8

import base64

# 对称密钥： 加密和解密的密钥相同
# RSA是三个人的名字的首字母， 是基于大素数乘积的因式分解求解困难的原理。
p='''MIICXwIBAAKBgQC45hzBBQ59JIfKfm2CbmyuYN7l7IQV46EsAgnnKaZ8henAEpP5
uSf22aQ6N1Yg86djgOe/c2oUjdec/uFnCGjVpGrrXbE5ZmH8M8vWWhQifn4RuY9A
nv8lX5c7w/kBf55qrTuQZF7O6xgEMuU0BqbMr+e/oTd1TvA0FCk/qbxa+QIDAQAB
AoGBAKVT3NIam2H6kBDYC0NdSYCCzcv5OAH6j9qx1/kCnQMrGl/MPNRGYx2ubdJA
OJsuQrYORSpDIM9QJUMUBKgENPeNhuCfv1C3vgJE+gTc6Cdx4wNWZEhH1FkCKOqc
YYUqWUwlmqgDTaMEyeDt0LJ6/xT67Ldjix9g6yeTquE7zYqBAkEA5J03Xm3qXrjE
DiNIq1Ggd2A1cif34hNrcI9Ooh0kzC1CV95VSQkaxAFN4voJD4pLqWl0G8car5EV
LekfTrq9pQJBAM8MTfPesGbDJH4qPYy7ka0K9x0MEtQ2IO8ygg+Y9p216I6CvcoN
2zcBBNfuqVLzMdKWQoDZgI8t4CvkigLwz8UCQQCC3/XomygG3eNu7IgXe31PmcY+
+d6Qj+l74K51ZBXCxU4rm15bl1i5SL3b6KPzP4qdC3+qv0rpozbqt4Byw7j5AkEA
vL5LxZdomZUlDDo3d7Z5exS25mzeMUPSzBrwA4X+sxBkGp3Go430G3U7VBkFlE+M
SJufrlQYZO1+IKUqxrl9vQJBALA9NRlUhbyrDUHcPPjB5bwQpV5AgfJqBQnuXX7G
Pp/3/cdQUC6mW+QzMFvyg9OgqHSkSLrqVoZDJwU/IpHDx7A='''

a=base64.b64decode(p)
print 'a.size:', len(a)

b='B03D35195485BCAB0D41DC3CF8C1E5BC10A55E4081F26A0509EE5D7EC63E9FF7FDC750502EA65BE433305BF283D3A0A874A448BAEA56864327053F2291C3C7B0'
print 'b.size:', len(b)/2*8

a='''MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgjC3Benii4JCWSHuZ36QFvih3afnCl5E+UGCDhiLjJPOgCgYIKoZIzj0DAQehRANCAARz4epY6QDv3xIg0BOKC/xGk5vYHlr11zU69FtQoNX6MhSuA1+6JoWB05j3oELqadCaqVeltf7JztaadEOqKz8M'''
b=base64.b64decode(a)
print 'b.size:', len(b)
print b