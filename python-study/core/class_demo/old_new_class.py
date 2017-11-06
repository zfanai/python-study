#!usr/bin/env python
# -*- coding: utf-8 -*

"""
old new class
1.
"""

#
class Debug(object):
    def __init__(self):
        pass
    def trace(self,msg):
        print "LanguageTest:", msg
debug=Debug()

#
class OldClass():
    pass

#
class NewClass(object):
    pass

def test():
    debug.trace(["test:start:"])
    
    #: 旧式类OldClass只是Class类的一个对象，并不是一种新的类型，实例也是实例对象
    oldclsobj = OldClass()
    #print (oldclsobj), type(OldClass)
    debug.trace(["test:oldclass:", oldclsobj, type(oldclsobj), oldclsobj.__class__, type(OldClass)]) # OldClass有类型，
    # （接上）但是没有类， 访问__class__没有此属性
    
    #:新式类NewClass定义了一种新的类型，创建的实例是这个类型的实例
    newclsobj = NewClass()
    #print (newclsobj), type(NewClass)
    debug.trace(["test:newclass:", newclsobj, type(newclsobj), newclsobj.__class__, type(NewClass), NewClass.__class__ , NewClass.__base__])
    print 'a:', type(object)
    
    # NOTE: 170322, 上面的说法可能不太准确吧。添加了新的打印信息后，对比更清晰一点。最权威的说法就是，新式类统一了类和类型，旧式类
    # type()函数获得类型， obj.__class__获得类， 是不一样的， 而类型是instance, 类就是用class定义的定义的类， 用class定义的类的类型是classobj

def func2():
    class Animal(object):
        pass
    class Dog(Animal):
        pass
    d=Dog()
    print 'd:', d, Dog.__base__, Dog.__subclasses__
    print 'f2:', Animal, object, Animal.__base__, type(object)
    # object,type 是两个特殊的实例， 自身是自身的实例
    print isinstance(object, object)   
    print isinstance(object, type)
    print isinstance(Dog, Dog)
    print object==type, id(object), id(type)
    a=object()
    # object 的实例不能直接赋值， 因为定义了__slots__属性
    print a,d
    #a.a=1
    #print a.a
    
if __name__ == "__main__":
    #print __doc__
    debug.trace(["main:start:"])
    #test()
    func2()