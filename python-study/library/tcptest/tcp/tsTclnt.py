#!/usr/bin/env python
#encoding:utf8

from socket import *

#HOST = 'localhost'
#PORT = 21567
HOST = '192.168.1.100'
PORT = 8088
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 客户端和服务端都需要关闭连接。
while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()
