#encoding:utf8

from tornado import httpclient, gen, ioloop, queues
from tornado.ioloop import IOLoop

def handle_response(response):
    if response.error:
        print("Error: %s" % response.error)
    else:
        print(response.body)
        
httpclient.AsyncHTTPClient().fetch('http://127.0.0.1:8880', handle_response)
#httpclient.HTTPClient().fetch('http://127.0.0.1:8880')
print 'client finish'
#a=raw_input()
IOLoop.instance().start()
