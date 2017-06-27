#!/usr/bin/env python
#coding=utf-8
import datetime 

'''
修饰器的用法。修饰器的灵感来自于类的静态函数的简要写法。
'''

class Debug(object):
    def trace(self, msg):
        dt=datetime.datetime.now()
        print "[%s]:%s"%(dt.strftime("%Y%m%d%H%M%S"), msg)
debug=Debug()

# 用内建函数staticmethod或使用@staticmethod修饰符是一样的效果
class MyClass(object):
    print 'MyClass'
    def staticFoo():
        print 'inside staticFoo' 
    staticFoo = staticmethod(staticFoo) 
    
    @staticmethod
    def staticFoo2():
        print 'inside staticFoo 2'
#
def decFunc(x,y):
    print 'decFunc'
    
    def inner2(x,y):
        print 'inner 2'
        print "x,y:",x,y
    
    #  返回的调用对象必须有一个参数是表示被修饰的函数
    def inner(f):
        print 'inner'
        #f(5,6)
        return inner2
        
    #返回的是一个函数对象，返回的对象必须是可以调用的
    return inner

# 装饰器语法，分为装饰函数decFunc和被修饰函数Func，
# 修饰器函数可以用数学形式f(g(x))函数来类比。
# 下面的写法等价于 (decFunc(1,2))(Func)
# 先调用装饰函数, 装饰器也有点像包装器，最好是像包装器这样来用它
# 但是它的内部起始就是换了一个可调用对象来执行.但是被修饰的函数本身会作为一个参数，传递到新的可调用对象中去
# decFunc修饰器会作为全局代码先解析。
# 下面这样写的代码就会全局被调用。
# 2016-7-29 上面的注释说得比较清楚，所以装饰器函数是先调用，得到的返回值再去当做一个调用对象去调用，以被修饰函数
# 作为参数。
@decFunc(1,2)
def Func(x,y):
    print 'Func' 
    print 'x,y:', x, y

#
def func1():
    #obj = MyClass()
    #obj.staticFoo()
    #obj.staticFoo2()
    #print 'start\n\n================'
    Func(3,4)
    pass

class Decor1(object):
    def __init__(self, func):
        self.func=func
        
    def __call__(self, *args, **kargs):
        debug.trace(['Decor1 __call__', args, kargs])
        return self.func

# 修饰器的核心是函数参数，影响是改变了函数的行为。
# 执行结果还是要看修饰器的内部结构。        
@Decor1
def func2(x,y):
    debug.trace(['x,y:', x, y])
    
def func3():
    # 无参数修饰器和参数修饰器的执行过程是不一样的。
    # @func3_decor()和@func3_decor是不一样的。
    def func3_decor():
        def wrapper(f):
            #f(x,y)
            return f
            
        return wrapper
    
    @func3_decor()
    def func3_1(x,y):
        print x,y
    #    
    func3_1(3,4)
        
if __name__ == '__main__':
    #func1()
    #func2(1,2)
    func3()
    