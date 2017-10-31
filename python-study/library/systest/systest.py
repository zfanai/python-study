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

# @note �����ж��Ƿ���Python3�汾��
def func3():
    PY3 = (sys.version_info[0] >= 3)
    debug.trace(['PY3:', PY3])

def func4():
    debug.trace(['attr of sys:', dir(sys)])
    
def func5():
    def inner_func1():
        print sys.exc_info()   # ��ǰ������쳣��Ϣ��
        #print sys.e
        print sys.exc_type
        #print sys.exc_value
        print 'inner_func1'
    def inner_func2():
        inner_func1()
    def inner_func3():
        inner_func2()
    def inner_func4():
        inner_func3()
    def inner_func5():
        inner_func4()
    inner_func5()
    
#
if __name__=='__main__':
    #func1()
    #func2()
    #func4()
    func5()