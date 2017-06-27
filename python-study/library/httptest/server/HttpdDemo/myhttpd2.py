#!/usr/bin/env python
#encoding:gbk

from os import curdir, sep
from BaseHTTPServer import \
    BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

import math

"""
���̵߳�HTTP������������ͻ���A�������������һ�����󣬶��������Ĵ���ʱ��ܳ�������˻�û�з�����Ӧ��
���ǿͻ���BҲ�������������һ�����󣬷������ǿ����������������ġ�
���ڵ������ǣ��ڷ�������û�з���A����Ӧ��ʱ���Ƿ���˵��������A������TCP���ӣ���B�����ʱ��������������Ĵ���
�������ֻ���B����TCP�����𡣷���������ͬʱ�������ͻ��˱���TCP�����𣬷�������ʹ�õ�ͬһ���˿�����Ϊ�ͻ���
������ͬһ���������˿ڷ�������
"""
class MyHandler(BaseHTTPRequestHandler):

    def delay(self):
        pass
        print self.path
        
        i,j = 0,0
        while i < 290:
            print i 
            i = i + 1
            j = 0
            
            #while j < 10000:
            while j < 100:
                j = j + 1
                print j,
            #print ""
    def look_inside(self):
        pass
        print self.path
        print "dir(MyHandler):",dir(self)
        print "client_address:",self.client_address,type(self.client_address)
        print "method:address_string:",self.address_string()
        print "connection:",self.connection,type(self.connection), dir(self.connection)
        print "connection:_sock:",self.connection._sock,type(self.connection._sock),dir(self.connection._sock)
        print "connection:_sock:getpeername:",self.connection._sock.getpeername()
        print "connection:_sock:getsockname:",self.connection._sock.getsockname()
        
        print "command:",self.command
        print "server:",self.server, type(self.server), dir(self.server)
            
    def do_GET(self):
        try:
            print "do_GET:start:"
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            
            #print self.path
            #print "dir(MyHandler):",dir(self)
            
            #self.look_inside()
            
            # �ڷ��ؽ��֮ǰ������һЩ������ʱ�� ��������̵߳�HTTPServer
            # �汾���бȽ�
            if self.path=="/index.html":
                #self.delay()
                pass
            
            #
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

# ���߳�
class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass
    
def main():
    try:
        #server = HTTPServer(('', 8000), MyHandler)
        server = ThreadingServer(('', 8100), MyHandler)
        print 'ThreadingServer'
        print 'Welcome to the machine...'
        print 'Press ^C once or twice to quit'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
