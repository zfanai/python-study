#!usr/bin/env python
# -*- coding: utf-8 -*
from zftrace import debug
'''
'''


def func1():
    class Animal(object):
        def __init__(self):
            print 'Animal.__init__'
            self.n=12
        def run(self):
            print 'Animal.run'
            
    class Dog(Animal):
        def __init__(self):
            print 'Dog.__init__', Animal.__init__, self
            #Animal.__init__(self)+
        def run(self):
            print 'Dog.run'
    class Car(object):pass
    
    # 类可以调用实例属性， 但必须是指定一个实例参数。
    d=Dog()
    c=Car() 
    a=Animal()

    print 'fuunc1:5.0:===='
    #debug.trace('app', '__init__:', Dog.__init__(d))
    Dog.__init__(d)
    print 'fuunc1:5.1:===='
    
    # 虽然Dog.__init__这是一个没有绑定的函数， 但是对一个参数的基本类型检查还是要有的， 就是必须是Dog的实例
    # 否则Python的类型系统就太松散了。
    #debug.trace('app', '__init__:', Dog.__init__(c))
    #print 'c.n:', c.n
    
    # a不是Dog的实例， 但是可以认为d是Animal的实例
    #debug.trace('app', '__init__:', Dog.__init__(a))
    #debug.trace('app', '__init__:', Animal.__init__(d))
    #print d.__init__()    # d.__init__的调用是Animal.__init__(d)调用的等价形式。本质上就是
    # 调用系统存在的一个属性， 然后然后有一些类型规范的约束。
    Animal.__init__(d)
    print 'fuunc1:5.2:===='
    
    # Animal.__init__是未绑定的函数， 如果调用这个函数， 跟根据具体的参数才能确定会执行哪个函数， 这就是多态。 (这一句话写错了， 实际情况不是的。)
    # Animal.__init__(d)调用的是Animal的__init__函数。
    print 'func1:6.1:', Animal.__init__, Dog.__init__, Animal.__init__==Dog.__init__, type(Animal.__init__)
    # a.__init__这种写法是绑定的方法， 如果借用量子力学的术语， 就是坍缩了的方法， 因为指定了对象， 
    print 'func1:6.2:', a.__init__, d.__init__
    print 'func1:6.3:', d, d.__init__()
    print 'func1:6.4:', d, Animal.__init__(d)
    
    
def func2():
    class Animal(object):
        def __init__(self):
            self.n=12
    f=lambda x:x

    a = Animal()
    #lambda self : self
    #Animal.f=
    def f2(self):
        self.c=3
        print 'f2'
    Animal.f2=f2
    print 'func2:1.1:', Animal.f2
    #
    #a = Animal()
    print a.f2()
    
    
if __name__ == "__main__":
    #func1()
    func2()
    