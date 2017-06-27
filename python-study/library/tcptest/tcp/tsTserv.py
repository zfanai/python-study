#!/usr/bin/env python
#encoding:gbk

from socket import *
from time import ctime
import threading

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)



def test_func1():
    pass
    # ����ʽ�����ӷ�ʽ����һ���ͻ�������֮�������ͻ������Ӳ���
    # ����ѭ���ķ�ʽ��
    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr
    
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (
                ctime(), data))
        
        tcpCliSock.close()
    
    # �ر��˷������Ķ˿�
    tcpSerSock.close()    

"""
�����������˵���ˣ�ͬһ�������socket��ȷʵ����accept������벻ͬ�Ŀͻ��˽���TCP���ӡ�
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
    
