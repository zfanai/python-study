#!usr/bin/env python
# -*- coding: utf-8 -*
from zftrace import debug
'''
'''


def func1():
    class Animal(object):
        def __init__(self):
            self.n=12
    class Dog(Animal):
        def __init__(self):pass
    class Car(object):pass
    
    # 类可以调用实例属性， 但必须是指定一个实例参数。
    d=Dog()
    c=Car() 
    a=Animal()
    
    debug.trace('app', '__init__:', Dog.__init__(d))
    
    # 虽然Dog.__init__这是一个没有绑定的函数， 但是对一个参数的基本类型检查还是要有的， 就是必须是Dog的实例
    # 否则Python的类型系统就太松散了。
    #debug.trace('app', '__init__:', Dog.__init__(c))
    #print 'c.n:', c.n
    
    # a不是Dog的实例， 但是可以认为d是Animal的实例
    #debug.trace('app', '__init__:', Dog.__init__(a))
    debug.trace('app', '__init__:', Animal.__init__(d))
    print d.__init__()    # d.__init__的调用是Animal.__init__(d)调用的等价形式。本质上就是
    # 调用系统存在的一个属性， 然后然后有一些类型规范的约束。
    
    
    
if __name__ == "__main__":
    func1()
    