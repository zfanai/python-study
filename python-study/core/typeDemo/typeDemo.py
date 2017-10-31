#!usr/bin/env python
# -*- coding: utf-8 -*

'''
类型和类之间的桥梁type(cls, (base,), {}),
为什么要写继承自type的类，可以做哪些事情。
'''

#
class Debug(object):
    def __init__(self):
        pass
    def trace(self,msg):
        print "LanguageTest:", msg
debug=Debug()


# obj->class->type<->type
# object是内建类型.内建类型的类型是type
# 用户自定义类型的类型type，表示是用class, 用户自定义类型可以看成是type类型的一个实例。
def func1():
    # Model是类名， (object,)指定基类, {'a':1}指定类属性。
    cls=type('Model', (object,), {'a':1})
    c=cls()
    debug.trace(['c.a:', c, c.a, cls, dir(c), dir(cls), cls.__bases__])
    debug.trace(['__class__:', c.__class__, cls.__class__, type(c.__class__), type(cls.__class__), isinstance(c.__class__, type)])
    debug.trace(['type:', type, type(type.__class__), type(type)])
    debug.trace(['object:', object, object.__class__, type(object)])
    a=object()
    b=1
    debug.trace(['object,a:', a, object, 'dd'.__class__, (1,).__class__])

# 旧式类的b.__class__和type(b)的结果是不一样的.
# 旧式类的type(b) 返回的是 instance类型。    
def func2():
    class Dog(object):
        pass
    d=Dog()
    debug.trace(['d:', d, type(d), Dog, dir(d)])


    
if __name__ == "__main__":
    debug.trace(["main:start:"])
    #func1()
    func2()
    