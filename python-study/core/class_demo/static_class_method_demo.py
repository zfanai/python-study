#!usr/bin/env python
# -*- coding: utf-8 -*

"""
static method and class method demo
1.类方法与静态方法基本上没什么区别，有一个不同的地方就是
类方法有一个默认的参数cls，表示当前的类
"""

class TestStaticMethod(object):
    
    def foo():
        print 'calling static method foo()'
    foo = staticmethod(foo)
    
    # NOTE: zhouf, 170322, 虽然定义的时候不会报错，但是不能正常的调用
    def foo2():pass
    foo2=staticmethod(foo2)   # 但是把它改成静态函数之后就可以正常访问了。

class TestClassMethod(object):
    def foo(cls):
        print "calling class method foo()"
        print "foo() is part of class:",cls.__name__
    foo = classmethod(foo)

class TestStaticMethodDecor(object):
    @staticmethod
    def foo():
        print 'calling static method foo()'
    #foo = staticmethod(foo)

class TestClassMethodDecor(object):
    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print "foo() is part of class:",cls.__name__
    #foo = classmethod(foo)
            
def test():
    # 类调用和实例调用都可以
    TestStaticMethod.foo()
    tsm = TestStaticMethod()
    tsm.foo()
    
    tcm =TestClassMethod()
    TestClassMethod.foo()
    tcm.foo()

def test2():
    t=TestStaticMethod()
    TestStaticMethod.foo2(t)
    
class Dog(object):
    # 下面这样写，可以定义，但是无法调用， 除非修饰成静态函数。
    def f():
        print 'dda'
        pass
        
    @staticmethod
    def f3():
        print 'f3'
        
    def f2(self):
        print 'dfa'
        
def func1():
    d=Dog()
    d.f2()
    #Dog.f()   #调用会出错
    print hasattr(Dog, 'f')
    print hasattr(d, 'f')
    
    #f=getattr(d, 'f')
    #f()   # 这样调用也会报错
    
    #Dog.f3(2)   # 不能带参数
    
    print dir(Dog)
    print dir(d)
    print Dog.__dict__
    print d.__dict__
    
    
if __name__ == "__main__":
    print "start ..."
    #test()
    #test2()
    func1()
    