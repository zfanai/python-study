#encoding:utf8
import tornado.httpserver  
import tornado.ioloop  
import tornado.web  
import tornado.options  
import os.path  
   
from tornado.options import define, options  
define("port", default=5000, help="run on the given port", type=int)  
   
class BaseHandler(tornado.web.RequestHandler):  
    def get_current_user(self):  
        return self.get_secure_cookie("username")  
    
class LoginHandler(BaseHandler):  
    def get(self):  
        self.render('login.html')  
    def post(self):  
        #print self.current_user
        self.set_secure_cookie("username", self.get_argument("username"))  
        #print self.current_user
        self.redirect("/") 

# 只要有cookie就认为是登录了, 登录状态跟cookie有关
class WelcomeHandler(BaseHandler):  
    @tornado.web.authenticated
    def get(self):  
        self.render('index.html', user=self.current_user)  
  
class LogoutHandler(BaseHandler):  
    def post(self):  
        if (self.get_argument("logout", None)):  
            self.clear_cookie("username")  
        self.redirect("/")  
        
if __name__ == "__main__":  
    tornado.options.parse_command_line()  
    settings = {  
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),  
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",  
        "login_url": "/login"  
    }  
    application = tornado.web.Application([  
        (r'/', WelcomeHandler),  
        (r'/login', LoginHandler),  
        (r'/logout', LogoutHandler)  
    ],debug= True,**settings)  
    http_server = tornado.httpserver.HTTPServer(application)  
    http_server.listen(options.port)  
    print options.port
    tornado.ioloop.IOLoop.instance().start()  