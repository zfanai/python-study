#!usr/bin/env python
# -*- coding: gbk -*

class Debug(object):
    def __init__(self):
        pass
    def trace(self, *msg):
        print "trace:", msg
debug=Debug()

class AnimalMeta(type):
    '''
    def __new__(cls, name, this_bases, d):
        debug.trace('__new__:', name, this_bases, d)
        return type.__new__(cls, name, this_bases, d)'''
    def __new__(cls, name, this_bases, d):
        debug.trace('__new__:AnimalMeta')
        return type.__new__(cls, name, this_bases, d)
        
        
    def __init__(cls, classname, bases, fields):
        debug.trace('__init__:', classname, bases, fields)
        type.__init__(cls, classname, bases, fields)

class AnimalClass(object):
    pass

def with_metacls(meta, *base):
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            debug.trace('__new__:', name, this_bases, d)
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, base, d)
    # 虽然都是创建类型的类，但是在__new__函数里面有可能又把类型换成了类型的父类。        
    #return  metaclass('Animal', base, {})
    return  metaclass('temporary_class', None, {})
#    
def func1():
    #AnimalCls=AnimalMeta('Animal', (object,), {})
    AnimalCls=with_metacls(AnimalMeta, AnimalClass)
    # 声明一个类时，其实也是表示创建一个类对象。
    debug.trace('before Dog')
    class Dog(AnimalCls):
        pass
        #color=2
    debug.trace('before Taidi')
    class Taidi(Dog):
        pass
        
# type可以作为元类的基类来使用的。
# AnimalMeta 是type的子类， 也可以通过 AnimalMeta（）调用来创建一个类。
def func2():
    # 
    class AnimalMeta(type):
        def __new__(cls, name, bases, attrs):
            debug.trace('AnimalMeta,__new__')
            return type.__new__(cls, name, bases, attrs)
    
    def with_metaclass(meta, *bases):
        """Create a base class with a metaclass."""
        # This requires a bit of explanation: the basic idea is to make a dummy
        # metaclass for one level of class instantiation that replaces itself with
        # the actual metaclass.
        class metaclass(meta):
            def __new__(cls, name, this_bases, d):
                debug.trace('metaclass,__new__')
                return meta(name, bases, d)
        # type是一个类型, __new__是一个实例方法， 其实应该说是Python针对不同的方法会绑定不同的对象。
        # 普通的实例方法绑定实例对象，类方法绑定类型对象（类）。    
        return type.__new__(metaclass, 'temporary_class', (), {})
    AnimalCls=with_metaclass(AnimalMeta)
    debug.trace('AnimalCls:', AnimalCls)
    class Dog(AnimalCls):
        def __init__(self, name):
            self.name=name
    d=Dog('kkk')
    print d
        
def func3():
    class AnimalMeta(type):
        # __new__会构造 AnimalMeta 这个元类的实例， 元类的实例就是类
        def __new__(cls, name, bases, attrs):
            debug.trace('AnimalMeta,__new__')
            return type.__new__(cls, name, bases, attrs)
    
    def run(self):
        print 'run'
    dog_cls=AnimalMeta('Dog', (object,), {'a':1, 'run':run})
    d=dog_cls()
    d.run()
    
if __name__=='__main__':
    #func2()
    func3()