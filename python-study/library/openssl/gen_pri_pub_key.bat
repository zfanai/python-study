:: ˽Կ
:: -des3 2048, ˽Կ�������ÿ����������� 
openssl genrsa -out ./myPrivateKey.pem -passout pass:"860102"
:: ��˽Կ���ɹ�Կ
:: -config openssl.cnf
openssl rsa -pubout -in ./myPrivateKey.pem -passin pass:"860102" -out ./myPublicKey.pem