#encoding:utf8

import tornado.ioloop
import tornado.web
import os
import math
import time
from tornado import gen
from tornado.concurrent import Future

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

def delay(second):
    sum=0
    i=0
    j=0
    t1=time.time()
    while second>0:
        i=0
        while i<2000/1.94:
            j=0
            while j<3000:
                sum+=math.sqrt(i+j)
                #print sum
                j += 1
            i+=1
        #print second
        second -= 1
    t2=time.time()
    print sum, t2-t1

def delay2():
    t1 = time.time()
    sum=0
    i,j=0,0
    while i<1000000:
        i += 1
        sum+=1
        j=0
        while j<100:
            j+=1
            sum+=2
    print sum,i,j

# 实验证明    
class MainHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def get(self):
        #self.write("Hello, world")
        #self.render("index.html")
        print 'get 1'
        delay(30)
        print 'get 2'
        self.write('hello python')
        #self.finish()
        
class MainHandler2(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("Hello, world")
        #self.render("index.html")
        self.write('hello python')
        self.finish()
f=Future()


class MainHandler3(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        cursor = self.get_argument("cursor", None)
        # Save the future returned by wait_for_messages so we can cancel
        # it in wait_for_messages
        print 'cor 1.1'
        
        #f.set_result('hello a')
        self.future = f
        messages = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write('hello b')
    
    def on_connection_close(self):
        #global_message_buffer.cancel_wait(self.future)
        pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], 
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=True,)

if __name__ == "__main__":
    app = make_app()
    app.listen(8880)
    tornado.ioloop.IOLoop.current().start()