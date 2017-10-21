#!/usr/bin/env python
#encoding:utf8
# -*- coding: utf-8 -*-
#用于规定字符编码，想要中文正常最好就加上这句

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
#巴拉巴拉import一大堆tornado的东西，反正都有用，原封不动即可

import pymongo
#这里是导入MongoDB

define("port", default=5000, help="run on the given port", type=int)
#定义监听的端口，随便挑个喜欢的数字吧

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
    
        conn = pymongo.Connection("localhost", 12345)
        self.db = conn["demo"]
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",)

    def post(self):
        import time
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        blog = dict()
        if title and content:
            blog['title'] = title
            blog['content'] = content
            blog['date'] = int(time.time())
            coll = self.application.db.blog
            coll.insert(blog)
            self.redirect('/blog')
        self.redirect('/')

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.blog
        blog = coll.find_one()
        if blog:
            self.render("blog.html",
            page_title = blog['title'],
            blog = blog,
            )
        else:
            self.redirect('/')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
