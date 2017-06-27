:: 私钥
:: -des3 2048, 私钥还可以用口令来保护。 
openssl genrsa -out ./myPrivateKey.pem -passout pass:"860102"
:: 用私钥生成公钥
:: -config openssl.cnf
openssl rsa -pubout -in ./myPrivateKey.pem -passin pass:"860102" -out ./myPublicKey.pem