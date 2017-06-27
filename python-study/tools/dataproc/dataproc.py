#encoding:gbk
import data1

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    a=data1.data
    debug.trace(['size:', len(a)])
    #debug.trace(['sliece:', a[100:120]])
    for i in range(110, 120):
        debug.trace(['data:', i, a[i]])

if __name__=='__main__':
    func1()
