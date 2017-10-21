#coding: utf-8
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import random
import time

from tornado.options import define, options  
define("port", default=6000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        (r"/", MainHandler),
        (r"/blog", BlogHandler),
        ]

        settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        )

        #conn = pymongo.Connection("localhost", 12345)
        #self.db = conn["demo"]
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #time.sleep(3600)
        #while True:pass
        self.render("index.html",)

    def post(self):
        
        pass
        '''title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        blog = dict()
        if title and content:
            blog['title'] = title
            blog['content'] = content
            blog['date'] = int(time.time())
            coll = self.application.db.blog
            coll.insert(blog)
            self.redirect('/blog')
        self.redirect('/')'''

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        self.render("blog.html",)
        '''
        coll = self.application.db.blog
        blog = coll.find_one()
        if blog:
            self.render("blog.html",
            page_title = blog['title'],
            blog = blog,
            )
        else:
            self.redirect('/')'''

def main():
    tornado.options.parse_command_line()
    app = Application()
    print options.port
    #app.listen(options.port)
    app.listen(5000)
    #app.listen(5001)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()