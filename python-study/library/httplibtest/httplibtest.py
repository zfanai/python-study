#encoding:gbk

import httplib

class Debug(object):
    def trace(self,msg):
        print msg
debug=Debug()

def func1():
    conn=httplib.HTTPConnection("192.168.30.26:5000")
    conn.request("GET", "/login")
    res=conn.getresponse()
    debug.trace(["status:", res.status])
    debug.trace(["reason:", res.reason])

def func2():
    conn=httplib.HTTPConnection("192.168.30.26:5001")
    conn.request("GET", "/test/page1")
    res=conn.getresponse()
    debug.trace(["res:", res, dir(res)])
    debug.trace(["status:", res.status])
    debug.trace(["reason:", res.reason])
    buf=res.read(-1)
    debug.trace(["buf:", buf])
    debug.trace(["header:", res.getheaders()])
    #debug.trace(["header:", res.getheader()])
    
if __name__=="__main__":
    #func1()
    func2()