#!/usr/bin/env python
#encoding:gbk

from os import curdir, sep
from BaseHTTPServer import \
    BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

import math

"""
多线程的HTTP服务器，如果客户端A向服务器发送了一个请求，而这个请求的处理时间很长，服务端还没有返回响应，
这是客户端B也向服务器发送了一个请求，服务器是可以立马处理这个请求的。
现在的疑问是，在服务器还没有返回A的响应的时候，是否是说服务器和A还保持TCP连接，而B在这个时候来请求服务器的处理，
服务器又会与B建立TCP连接吗。服务器可以同时与两个客户端保持TCP连接吗，服务器是使用的同一个端口吗。因为客户端
都是向同一个服务器端口发送请求
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
            
            # 在返回结果之前，增加一些处理延时， 用来与多线程的HTTPServer
            # 版本进行比较
            if self.path=="/index.html":
                #self.delay()
                pass
            
            #
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

# 多线程
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
