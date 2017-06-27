#encoding:utf8

class Debug(object):
    def trace(self, msg):
        print "trace:", msg
    def rprint(self, msg):
        print msg
debug=Debug()

def func1():
    f=open("aquila012_103333333_1.05.hex")
    tmp=f.readlines()
    f.close()
    #debug.trace([tmp])
    debug.trace([tmp[1759]])

if __name__=="__main__":
    func1()