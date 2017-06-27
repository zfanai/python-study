#!/usr/bin/env python
#encoding:gbk

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

def test_func1():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send('%s\r\n' % data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data.strip()
        tcpCliSock.close()      

def test_func2():
    while True:
        print "start connect server..."
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        
        while True:
            data = raw_input('> ')
            if not data:
                break
            tcpCliSock.send('%s\r\n' % data)
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            print data.strip()
        
        print "data:",data,type(data)
        if data=="bye":
            break
        
        # 关闭连接
        tcpCliSock.close() 
        
# 主函数
if __name__=="__main__":
    pass
    test_func1()
    #test_func2()
    
