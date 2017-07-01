#!/usr/bin/env python
#encoding:utf8
import json
from os import curdir, sep
from BaseHTTPServer import \
    BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def delay(self):
        pass
        print self.path
        
        i,j = 0,0
        while i < 100:
            print i 
            i = i + 1
            j = 0
            
            #while j < 10000:
            while j < 10:
                j = j + 1
                print j
                
    def do_GET(self):
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            
            # 在返回结果之前，增加一些处理延时， 用来与多线程的HTTPServer
            # 版本进行比较
            #self.delay()
            
            # 返回结果
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
    def do_POST(self):
        #for k in dir(self):print 'k:', k
        #print 'request:', self.request
        print 'body:', self.rfile.read(int(self.headers.getheader('content-length', 0)))
        #print 'request lines:', self.raw_requestline
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps({'res':'OK'}, ensure_ascii=False))

def main():
    try:
        server = HTTPServer(('', 5000), MyHandler)
        print 'Welcome to the machine...'
        print 'Press ^C once or twice to quit'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
