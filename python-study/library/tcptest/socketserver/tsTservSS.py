#!/usr/bin/env python
#encoding:gbk

from SocketServer import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

from SocketServer import ThreadingMixIn

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(),
        self.rfile.readline()))

# ������һ���ͻ���һֱռ�÷���˵����ӣ���һ���Ŷ�ϵͳ��
# �����ǰ�������A�ͻ������ӣ�����B�ͻ���Ҳ�������ӷ���ˣ���ô����Aͨ�ŵĿ���ʱ���п��ܶϿ���A�����ӣ����ĳ���B����
# ����TCP���ӣ�

"""
1.����TCPServer�Ĵ���ʽ���ǣ�ÿ���յ�һ��TCP����֮��Ͱ�TCP���ӹر���

"""

# ���߳�
def test_func1():
    pass
    tcpServ = TCP(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()

# ���߳�����
class ThreadingServer(ThreadingMixIn, TCP):
    pass

def test_func2():
    pass    
    tcpServ = ThreadingServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()

if __name__=="__main__":
    pass
    test_func1()
    
