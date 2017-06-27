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

# 不会让一个客户端一直占用服务端的连接，有一个排队系统，
# 如果当前服务端与A客户端连接，但是B客户端也尝试连接服务端，那么在与A通信的空闲时候，有可能断开与A的连接，而改成与B连接
# 管理TCP连接，

"""
1.怀疑TCPServer的处理方式就是，每次收到一个TCP数据之后就把TCP连接关闭了

"""

# 单线程
def test_func1():
    pass
    tcpServ = TCP(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()

# 多线程特性
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
    
