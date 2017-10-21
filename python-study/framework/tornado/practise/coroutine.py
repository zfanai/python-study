#encoding:utf8

import time
from datetime import timedelta

try:
    from HTMLParser import HTMLParser
    from urlparse import urljoin, urldefrag
except ImportError:
    from html.parser import HTMLParser
    from urllib.parse import urljoin, urldefrag

from tornado.concurrent import Future
from tornado import httpclient, gen, ioloop, queues

fut=Future()
fut2=Future()

def handle_response(response):
    if response.error:
        print("Error: %s" % response.error)
    else:
        print(response.body)
    fut.set_result(123)

# AsyncHTTPClient  实现的基础也是Future机制
@gen.coroutine
def main2():
    print 'm:1'
    # AsyncHTTPClient 如果是在yield后面使用， 就会等待， 但是并不是阻塞， 其他协程可以使用。
    res=httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880', handle_response)
    #res = httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880')
    print 'm:res:', res
    a=yield  res    
    # 生成器调用next之后， yield后面的值会作为next函数的返回值返回， 
    # 但是生成器就会停留在这里了。 包括等号的赋值运行也没有进行
    # 直到下次调用生成器的next函数或send函数， send函数可以给生成器的继续执行传递一个参数， 赋值给yield表达式
    # 左边的变量。
    print 'm:2', a
    #yield Future()
    print 'm:3'


# AsyncHTTPClient  实现的基础也是Future机制
@gen.coroutine
def main():
    print 'm:1'
    # AsyncHTTPClient 如果是在yield后面使用， 就会等待， 但是并不是阻塞， 其他协程可以使用。
    #res=httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880', handle_response)
    #res = httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880')
    #print 'm:res:', res
    #a=yield  res    
    # 生成器调用next之后， yield后面的值会作为next函数的返回值返回， 
    # 但是生成器就会停留在这里了。 包括等号的赋值运行也没有进行
    # 直到下次调用生成器的next函数或send函数， send函数可以给生成器的继续执行传递一个参数， 赋值给yield表达式
    # 左边的变量。
    #print 'm:2', a
    #httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880', handle_response)
    print 'm:2'
    
    a=yield fut
    print 'm:3', a

print type(main)    

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    def f():
        print 'add cb:', 1
        #
    io_loop.add_callback(f)
    def cb():
        print 'cb'
        fut.set_result(112)
        fut2.set_result(113)
    io_loop.add_timeout(time.time()+2, cb)
    print type(io_loop)
    def cb2(fu):
        print 'cb2:', fu
    #io_loop.add_future(fut2, cb2)
    #fut2.set_result(2)
    io_loop.run_sync(main)