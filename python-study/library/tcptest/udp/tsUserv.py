#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

# UDP通信不会跟客户端建立连接，所以可以接受多个客户端的信息。
# 有信息来接受，相当于微信，短信。
while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (
        ctime(), data), addr)
    print '...received from and returned to:', addr

udpSerSock.close()
