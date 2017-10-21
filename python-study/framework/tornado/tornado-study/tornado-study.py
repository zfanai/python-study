#!/usr/bin/env python
#encoding:utf8
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import uuid

from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line

from zftrace import debug

define("port", default=5000, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


class BaseHandler(tornado.web.RequestHandler):
    '''
    def get_current_user(self):
        user_json = self.get_secure_cookie("chatdemo_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)'''


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #print 'MainHandler'
        #self.render("index.html", messages=global_message_buffer.cache)
        self.render("index.html", title='index')

def delay():
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
class Test1Handler(BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        #print 'MainHandler'
        #self.render("index.html", messages=global_message_buffer.cache)
       
        #delay()
            
        self.render("index.html", title='test1')

class Test2Handler(BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        #print 'MainHandler'
        #self.render("index.html", messages=global_message_buffer.cache)
        
        self.render("index.html", title='test2')        
        
# tornado.auth.GoogleMixin        
# asynchronous, 用这个修饰器，不是用了这个修饰器，这个函数就是异步执行的了
# 其实这个接口不加asynchronous同样也不会阻塞。
class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    #@tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self._on_auth)
            return
        debug.trace('app', 'AuthLoginHandler 1')
        self.authenticate_redirect()
        debug.trace('app', 'AuthLoginHandler 2')
        
def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/test1", Test1Handler),
            (r"/test2", Test2Handler),
            (r"/auth/login", AuthLoginHandler),
            #(r"/auth/logout", AuthLogoutHandler),
            #(r"/a/message/new", MessageNewHandler),
            #(r"/a/message/updates", MessageUpdatesHandler),
            ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url="/auth/login",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
        )
    app.listen(options.port)
    print 'dddd', options.port
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
