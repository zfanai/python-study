#!usr/bin/env python
# -*- coding: utf-8 -*

"""
__init__, __new__
"""

############################################################
## __new__是在构造对象时调用，__init__是被__new__调用的，如果重载了__new__
## 而没有在__new__里面调用__init__，则__init__不会调用，__new__必须返回一个
## 对象，如果没有返回对象，则会返回默认的None
## 170322， __new__负责构造对象， __init__负责初始化对象。
############################################################
class A(object):
    def __init__(self):
        print "in __init__"
        print A
        
    #print A
    def __new__(self):
        print "A,__new__", A
        print self, type(self)
        if self==A:print 'self==A'  #self跟A是相等的
        print "in __new__" 

class B(object):
    def __init__(self):
        print "in __init__"
        print B
    
    #print B  # 错误，不能访问类B
    
    def func1(self):
        print "B,func1", B  #可以访问类B
        
class Person(object):
    """Silly Person"""
 
    def __new__(cls, name, age):
        print '__new__ called.'
        
        print "Person,__new__:",Person, cls
        print 'super(Person, cls):', super(Person, cls)
        return super(Person, cls).__new__(cls, name, age)  # super函数的用法
        #return super(Person, cls).__new__(name, age)   #错误的
    
 
    def __init__(self, name, age):
        print '__init__ called.'
        self.name = name
        self.age = age
 
 
    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

class inch(float):
    "Convert from inch to meter"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)

 
class inch2(float):
    "THIS DOESN'T WORK!!!"
    def __init__(self, arg=0.0):
        float.__init__(self, arg*0.0254)

class ClassA(object):
    def __new__(cls):
        Object = super(ClassA, cls).__new__(cls)
        print "in New"
        return Object
    
    def __init__(self):
        print "in init"

class A1(object):pass        
def test1():
    obj = A()
    a1=A1()
    print a1, type(a1)

def test2():    
    obj = B()
    obj.func1()
    print obj

def test3():
    person = Person("Mike",23)
    print person

def test4():
    print inch(12)
    
def test5():
    print inch2(12)

if __name__ == "__main__":
    print __doc__
    #test1()
    test3()