#encoding:gbk
import datetime

class Debug(object):
    def trace(self, msg):
        dt=datetime.datetime.now()
        print "[%s]:%s" % (dt.strftime('%Y%m%d%H%M%S'), msg)
debug=Debug()

def func1():
    rv=filter(lambda x:x>0, [1,2,5,-1])
    debug.trace(['rv:', rv])

def func2():
    a=[[1,2],[3,4]]
    #b=map(lambda x:([x[1]],return [6]), a)
    #b=map(lambda x:x, a)
    for p in a:p[1]=6
    b=a
    debug.trace(['b:', b])
    
if __name__=='__main__':
    func2()