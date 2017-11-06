#encoding:utf8

"""
1. _xx形式的变量不能导入, from m1 import *  默认是不导入的，如果没有明确指定__all__变量的话。
2. __xx形式的变量系统会加上一个前缀_cls(外部访问的时候)
3. __xx__形式的变量虽然可以建议，但是编程规范不应该这样命名，因为系统的一个特殊变量是这样
命名的，容易引起混淆。
"""

from m1 import *
from m1 import car


class Debug(object):
    def trace(self,msg):
        print 'trace:',msg
debug=Debug()

debug.trace(['car._color:', car._color]) 
class Dog(object):
    def __init__(self):
        self.__x=1
        self.__y__=1
    def _run(self):
        debug.trace('_run')
        print '__y__:', self.__y__

def func1():
    d=Dog()
    #debug.trace(['d.__x:', d.__x])
    d._run()
    #debug.trace(['_VER:', _VER])
    debug.trace(['VER:', VER])
    #debug.trace(['NAME:', _NAME])
    debug.trace(['car:', car])
    
def func2():
    from m2 import *
    print a

if __name__ == '__main__':
    func2()
    


