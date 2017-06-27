#coding=utf8  
import socket  
import gevent  
from gevent.core import loop  
  
def f():  
    s, address = sock.accept()  
    print address  
    s.send("hello world\r\n")  
  
loop = loop()  
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sock.bind(("localhost",8030))  
sock.listen(10)  
io = loop.io(sock.fileno(),1) #1代表read  
io.start(f)  
loop.run()