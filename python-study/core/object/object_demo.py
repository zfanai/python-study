#encoding:utf8
import inspect

def func1():
    # object的实例不能直接设置属性
    o=object()
    print 'o:1:', o
    #o.name='x'
    
    # 但是从object继承的类的实例可以设置属性
    class Object(object):pass
    a=Object()
    a.name=2
    
    # 但是如果设置了__slots__
    class ObjCls(object):
        __slots__=()
    b=ObjCls()
    b.name='ddf'
    
    # list, object, dict都是如此
    
def func2():
    # Cls1有__slots__属性， Cls2继承自Cls1, Cls2没有__slots__属性
    # 静态定义的__slots__属性会决定类是否有__dict__属性， 类是否有__dict__属性决定决定类的实例是否可以设置属性
    class A(object):
        __slots__=()
        p=12
    class B(A):
        pass
    #
    print 'dir(A):', dir(A)
    print 'dir(B):', dir(B)
    
    print 'A.__dict__:', A.__dict__
    print 'B.__dict__:', B.__dict__
    
    #
    a=A()
    #a.name='dfd'
    print 'a.p:', a.p, A.p
    
    #
    b=B()
    b.name=23
    print 'b.p:', b.p, B.p
    print 'dir(b):', dir(b)
    #print 
    for p,v in vars(b).iteritems():
        print p,':', v
    
    B.__slots__=('x')
    for p,v in inspect.getmembers(b):
        print p,':', v
    
    b.name=45
    b1=B()
    b1.name=11
    
    #for p,v in inspect.getmembers(b1):
    #    print p,':', v

# dir和__dict__的区别。dir和__dict__的区别是很大的。
def func3():
    class A(object):
        pass
        __slots__=('a', 's')
        
    # A定义了__slots__属性， 并不是表示A没有了__dict__属性， 而是表明__dict__的值没有了__dict__属性。
    # __dict__的值没有了__dict__属性, 它的实例就不能设置属性了， 这两者是关联的。它的实例也没有了__dict__属性
    # 但是A依然是可以设置属性的。
    A.ss=1    # 类似于A是a的原型， A设置的属性可以影响到a, 但是如果a设置了ss属性后， A.ss的设置就不会影响到a.ss了
    # dir(A)里面虽然没有__dict__字段， 但是A.__dict__是可以访问的， 不然A.ss就不能起作用了。
    print 'A.__dict__:', A.__dict__
    print 'dir(A):', dir(A), '__dict__' in dir(A)
    # 
    for p,v in inspect.getmembers(A):
        print p,':', v
        
    a=A()
    #print 'a.__dict__:', a.__dict__
    print 'dir(a):', dir(a), a.ss
    #A.ss=2
    print 'a.ss:', a.ss
    a.s=3
    #A.a=4
    print 'a.ss:1:', a.s

def func4():
    class A(object):
        pass
    a=A()
    A.a=3
    print 'a.a:1:', a.a
    a.a=4
    print 'a.a:2:', a.a
    # 在a设置了a属性后， A.a就不会影响a.a了
    # JavaScript也是这样的特性， 
    A.a=5
    print 'a.a:3:', a.a
    
    
if __name__=='__main__':
    func3()