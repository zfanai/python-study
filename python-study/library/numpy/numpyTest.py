#encoding:utf8
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

#print '编码'
import numpy

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    x=numpy.array([[1,2,3], [4,5,6]], numpy.int32)
    debug.trace(type(x))

def func2():
    a=[1,4,5]
    avg=numpy.average(a)
    debug.trace(['avg:', avg])
    sd1=numpy.std(a)
    var1=numpy.var(a)
    #debug.trace(['sd1:', sd1])
    b=map(lambda x:x*3, a)
    debug.trace(['b:', b])
    sd2=numpy.std(b)
    var2=numpy.var(b)
    debug.trace(['sd:', sd1, sd2, sd2/sd1])
    debug.trace(['var:', var1, var2, var2/var1])
    
if __name__=='__main__':
    func2()