from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
#from yourapplication import app

from app import app
#from app.app_cfg import port
#from app.middle import push
app.debug = True

print('tornado run 1')
http_server = HTTPServer(WSGIContainer(app), ssl_options={
    'keyfile':'server.key',
    'certfile':'server.crt',
})
print('tornado run 2')
http_server.listen(int(5000))
print('tornado run 3')
IOLoop.instance().start()
print('tornado run 4')