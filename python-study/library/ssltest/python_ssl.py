import socket, ssl, pprint
import time

#cacrtf="ca/ca.crt"
#crtf="ca/server.crt"
#keyf="ca/server.key"
cacrtf="apns_development.pem"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(socket, ca_certs=cacrtf, cert_reqs=ssl.CERT_REQUIRED)
ssl_socket.connect(('127.0.0.1', 10023))

print repr(ssl_socket.getpeername())
print ssl_socket.cipher()
print pprint.pformat(ssl_socket.getpeercert())

ssl_socket.write("Time: %s\r\n" % time.time())

data = ssl_socket.read()
print data

ssl_socket.close()