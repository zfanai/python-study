set OPENSSL_CNF=%APACHE_DIR%\conf\openssl.cnf
openssl req -config "%OPENSSL_CNF%" -new -x509 -keyout key.pem -out cert.pem -days 365