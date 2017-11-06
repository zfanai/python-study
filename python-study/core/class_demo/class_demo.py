#!usr/bin/env python
# -*- coding: utf-8 -*

'''
1.这个文件主要测试了把一个类型赋给另一个类作为实例变量的例子。在Python里面类也是一种对象，可以像变量一样随意传递。
类的类型是类型。
2.第二个例子演示了对象的__setattr__和_getattr__函数可以重写，以达到修改类的.操作行为的目的。
'''

import traceback
#
class Debug(object):
    def __init__(self):
        pass
    def trace(self,msg):
        print "LanguageTest:", msg
debug=Debug()

#
class BaseQuery(object):
    def __init__(self):
        pass
    def action1(self):
        pass
#
class ClassDemo(object):
    def __init__(self):
        self.Query = BaseQuery
        pass
    
    def add(self,a,b):
        return a+b
#
def func1():
    debug.trace(["func1:start:"])
    demo = ClassDemo()
    debug.trace([ "func1:demo dir:", dir(demo) ])
    debug.trace([ "func1:demo,type:", type(demo), type(ClassDemo) ])
    
##########################################################
## @note 类的__setattr__, __getattr__, __str__函数的用法
## 对象在访问一个属性时，会调用__getattr__函数,这个特性可以由编程语言来模拟，
## 但是Python已经把它集成到语言特性里面去了。
##########################################################
class Book(object):
    #print "Class Book"
    #print dir(Book)
    #print object.
    #object.__getattribute__("name2")
    
    def __setattr__(self, name, value):
        #print dir(object)
        debug.trace(["Book:__setattr__:start:"])
        
        # 还是调用object的函数
        if name == 'value':
            object.__setattr__(self, name, value - 100)
        else:
            object.__setattr__(self, name, value)
    
    # python里面有没有这个特殊属性需要去查证一下。
    def __setattribute__(self, name, value):
        print '__setattribute__ start:'
    
    # 最终所有的属性访问的操纵都是在object.__getattribute__这个函数里面完成的。
    # 这个函数也是所有对象访问属性时必定调用的函数，而__getattr__函数是在__getattribute__里面被调用的
    # 只有在发现对象无法访问指定的属性时，就会调用这个回调函数。
    def __getattribute__(self, name):
        print '__getattribute__ start:2:', name
        print '__getattribute__:3:'
        #return object.__getattribute__(self, name)    # 并没有发生无限递归
        #val=object.x__xgetattr_._(self, name)
        #val=object.xx(self,'xx')    # 这个地方是触发了属性异常, 恰好就调用__getattr__进行处理。
        try:
            #val=object.__getattr__(self, name)   # object是没有__getattr__属性的，只有__setattr__属性。
            print '__getattribute__:4:'
            #self.__getattr__(name)     # 这样就肯定会形成嵌套递归。在这一句本身就会发生无限递归。调用了点号操作符。
            #self.__dict__['__getattr__'](name)
        except Exception,e:
            print 'e:', e
        #print 'val:', val
        print 'val:'
        #return object.__getattribute__(self, name)
        return 0
        
    # 没有找到属性时, 在__getattribute__函数捕捉到属性异常的时候， 会调用__getattr__函数。
    def __getattr__(self, name):
        # __getattribute__函数也应该是两个参数， 必须指定对象实例。
        # 下面这样写是没有意义的，为什么这样写不会发生递归现象， 肯定是内部处理机制避免了.
        # 也有可能__getattribute__和__getattr__不是直接的函数调用关系，但是在机制上的区别是
        # 对象访问任何对象时都会调用__getattribute__， 而在对象访问的属性不存在时，就会触发__getattr__。
        print '__getattrx__ start:', name
        return object.__getattribute__(self, name)    # 
        #return self.__getattribute__(self, name)   # 这样就肯定会触发无限递归， object.__getattribute__和self.__getattribute__是不相同的两个函数。
    
        try:
            print '__getattr__ start:', name
            return object.__getattribute__(name)
        except:
            return name + ' is not found!'
    
    def __str__(self):
        return self.name + ' cost : ' + str(self.value)

def func2():
    debug.trace(["func2:start:"])
    #print dir(Book)
    debug.trace(["func2:Book dir:", dir(Book)])
    c = Book()
    c.name = 'Python'
    c.value = 300
    
    #print c.name
    #print c.value
    #print str(c)
    #print c.Type
    debug.trace(["func2:c.name:", c.name1])
    debug.trace(["func2:c.value:", c.value])
    debug.trace(["func2:str(c):", str(c)])
    #debug.trace(["func2:c.Type:", c.Type])
    #
    object.__setattr__(c, "name2", "123")

class Car(object):
    color='white'

# 类属性和实例属性。引用一个对象的属性先从对象自身去查找有没有这个属性。
# 如果没有，再从它的类去查找有没有这个属性。
def func3():
    c=Car()
    ca=Car()
    debug.trace(['__mro__:', Car.__mro__])
    debug.trace(['c.color:', c.color, dir(c)])
    debug.trace(['Car.color:', Car.color, dir(Car)])
    debug.trace(['ca.color:', ca.color])
    print '=======\n'
    c.color='black'  # 给这个对象设置了color属性。
    debug.trace(['c.color:', c.color])
    debug.trace(['Car.color:', Car.color])
    debug.trace(['ca.color:', ca.color])
    print '=======\n'
    Car.color='red'
    debug.trace(['c.color:', c.color])
    debug.trace(['Car.color:', Car.color])
    debug.trace(['ca.color:', ca.color])

# 类似于JavaScript的apply函数。
class TestCls(object):
    # 引用不了tfunc1
    #
    def __init__(self, a):
        self.v=2
    
    # @note 起始函数都是单独的个体，只是类实例在调用函数的时候会默认
    # 把实例对象传递给这个函数，在语法上带来一定的简洁性。
    def _tfunc1(self):
        debug.trace(['tfunc1 method v:', self.v])
    #
    e={'a':_tfunc1}    
    debug.trace(['tfunc1:', _tfunc1])
        
def func4():
    #t=TestCls()
    t=TestCls(2)
    TestCls.e['a'](t)
    #t.tfunc1()
    pass

def func5():
    class Dog(object):pass
    d=Dog()
    #object.xx(d, 'xx')
    #object.__setattribute__(d, 'xx', 1)   # object 是没有__setattribute__属性的
    object.__setattr__(d, 'xx', 2)
    print 'd.xx:', d.xx
    d.aa=23
    v=object.__getattribute__(d, 'aa')    #属性异常
    print 'v:1:', v

'''
__getattribute__ 这个钩子的优先级更高， 
如果这个函数里面抛出一个异常， 那么__getattr__这个钩子就会执行
'''
def func6():
    class Dog(object):
        def __getattr__(self, name):
            print 'ga:', name
            #return self.x    # 无线递归
            object.__getattribute__(self, name)  # 这个不会递归
            #getattr(self, name)   # 效果相当于 self.[name] 
            # getattr和点操作符是一样的， 只不过getattr可以使用属性名变量。
            #return self.__dict__[name]  # 无线递归
        
        def __getattribute__(self, name):
            print 'gab:', name
            raise AttributeError
    d=Dog()
    print d.a
    

    
if __name__ == "__main__":
    debug.trace(["main:start:"])
    #func1()
    #func2()
    #func3()
    #func4()
    #func5()
    func6()
    