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

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            #xsrf_cookies=True,
            autoescape="xhtml_escape",
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    # 取得当前用户
    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)


# 新用户连接的处理类
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # 返回cache中的消息
        self.render("index.html", messages=MessageMixin.cache)

# 消息处理类
class MessageMixin(object):
    # waiters是一个set类型数据，存储着所有客户端挂起的连接
    # 当有新消息时，就会挨个发送给这些挂起的连接
    waiters = set()
    # 消息的cache
    cache = []
    # 服务端最大缓存的消息大小
    cache_size = 200

    def wait_for_messages(self, callback, cursor=None):
        # callback是客户端poll消息时的处理函数
        # 每次客户端连接的callback都不一样
        # 因为长连接的客户端从服务端获取消息后，会重新请求消息
        cls = MessageMixin
        # cursor是客户端保存的最新一条消息的id
        if cursor:
            index = 0
            # 查找最新一条消息在cache里的index
            for i in xrange(len(cls.cache)):
                index = len(cls.cache) - i - 1
                if cls.cache[index]["id"] == cursor:
                    break
            # 此处recent查找的是，客户端保存的最新消息的下一条消息
            # 但在DEBUG过程中一直没有数据
            # 是否是为某些客户端无法返回最新的cursor给服务端而准备的？？？
            # 这样就能返回在那个cursor之后的数据了？？？
            recent = cls.cache[index + 1:]
            if recent:
                callback(recent)
                return
        # 将callback加入到等待的连接列表中
        cls.waiters.add(callback)

    def cancel_wait(self, callback):
        # 客户端断开连接，从等待列表中移除相应的回调函数
        cls = MessageMixin
        cls.waiters.remove(callback)

    def new_messages(self, messages):
        cls = MessageMixin
        logging.info("Sending new message to %r listeners", len(cls.waiters))
        # 有新消息时，从回调列表中逐个处理已经连接的客户端
        for callback in cls.waiters:
            try:
                callback(messages)
            except:
                logging.error("Error in waiter callback", exc_info=True)
        # 清空回调列表，因为一个完整的长连接请求已处理完毕
        # 客户端再次发起ajax请求时，会再次在waiters中加入回调函数
        cls.waiters = set()
        # 将新消息加入到消息cache
        cls.cache.extend(messages)
        # 如果超过了总的cache大小则只取self.cache_size大小
        if len(cls.cache) > self.cache_size:
            cls.cache = cls.cache[-self.cache_size:]


# 处理新消息的类
class MessageNewHandler(BaseHandler, MessageMixin):
    #@tornado.web.authenticated
    def post(self):
        # message字典
        message = {
            "id": str(uuid.uuid4()),
            "from": self.current_user["first_name"],
            "body": self.get_argument("body"),
        }
        # 将渲染后的新消息内容加入到message字典中
        message["html"] = self.render_string("message.html", message=message)
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            # 将处理过后的新消息返回给客户端
            self.write(message)
        # 将新消息返回给所有保持长连接等待的客户端
        self.new_messages([message])


# 处理客户端长连接的类
class MessageUpdatesHandler(BaseHandler, MessageMixin):
    #@tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        # 得到客户端的cursor
        cursor = self.get_argument("cursor", None)
        # 将回调加入到回调列表，之后此次请求进入pending状态
        # 等待有新消息时，new_messages函数调用回调(on_new_messages)
        self.wait_for_messages(self.on_new_messages,
                               cursor=cursor)

    def on_new_messages(self, messages):
        # 挂起连接的回调函数，返回内容给客户端
        # Closed client connection
        # 判断客户端是否断开
        if self.request.connection.stream.closed():
            return
        # 将内容返回给客户端
        self.finish(dict(messages=messages))

    # 如果客户端关闭连接
    # 做简单的清理工作
    def on_connection_close(self):
        self.cancel_wait(self.on_new_messages)


#class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
class AuthLoginHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
#        if self.get_argument("openid.mode", None):
#            self.get_authenticated_user(self.async_callback(self._on_auth))
#            return
#        self.authenticate_redirect(ax_attrs=["name"])
        # 跳过google认证
        random_str = str(random.randint(1, 999999))
        self._on_auth({'email': 'roy.lieu@gmail.com',
                       'first_name': 'user' + '-' + random_str,
                       'last_name': 'lieu',
                       'name': 'user' + '-' + random_str})

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        self.set_secure_cookie("user", tornado.escape.json_encode(user))
        self.redirect("/")


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.write("You are now logged out")


def main():
    tornado.options.parse_command_line()
    app = Application()
    #app.listen(options.port)
    app.listen(5000)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()