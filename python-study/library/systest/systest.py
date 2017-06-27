#encoding:gbk
import sys

class Debug(object):
    def trace(self,obj):
        print 'trace:',obj
debug=Debug()

def func1():
    sp=sys.path
    debug.trace(['sp:', sp])
    
def func2():
    for p in sys.path:
        debug.trace(p)

# @note 用于判断是否是Python3版本。
def func3():
    PY3 = (sys.version_info[0] >= 3)
    debug.trace(['PY3:', PY3])

def func4():
    debug.trace(['attr of sys:', dir(sys)])
    
#
if __name__=='__main__':
    #func1()
    #func2()
    func4()