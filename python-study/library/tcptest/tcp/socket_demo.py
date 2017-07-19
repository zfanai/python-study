#!/usr/bin/env python
#encoding:utf8

from socket import *
from time import ctime
import threading


HOST = ''
#PORT = 21567 
PORT = 5000
BUFSIZ = 2048
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
#s.listen(LISTEN_QUEUE)  # werkzueg的用法
tcpSerSock.listen(5)

print 'waiting for connection...'
tcpCliSock, addr = tcpSerSock.accept()    #accept是阻塞式的， 但是可以多线程accept, select是非阻塞式的
print '...connected from:', addr