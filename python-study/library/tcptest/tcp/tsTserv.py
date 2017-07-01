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
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)



def test_func1():
    pass
    # 阻塞式的连接方式，与一个客户端连接之后，其他客户端连接不了
    # 无线循环的方式了
    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr
    
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            if not data:
                break
            #tcpCliSock.send('[%s] %s' % (
            #    ctime(), data))
        
        tcpCliSock.close()
    
    # 关闭了服务器的端口
    tcpSerSock.close()    

"""
下面这个函数说明了，同一个服务端socket，确实可以accept多次来与不同的客户端建立TCP连接。
"""
def test_func2():
    pass
    threads = []
    
    #thread.start_new_thread(test_func1, ())
    #thread.start_new_thread(test_func1, ())
    
    
    t1=threading.Thread(target=test_func1,
        args=())
    t2=threading.Thread(target=test_func1,
        args=())
    threads.append(t1)
    threads.append(t2)
    
    nloops=range(len(threads))
    
    for i in nloops:            # start threads
        threads[i].start()

    for i in nloops:            # wait for all
        threads[i].join()       # threads to finish
    
    print "test_func2 end:"

if __name__ == "__main__":
    pass
    test_func1()
    #test_func2()
    
