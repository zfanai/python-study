#encoding:gbk
'''
2016-8-1 getattr是函数，可以获得某个对象的属性，__getattr__是重载函数
在对象访问属性时被调用。
'''
class C():
#class C(object):  
    a = 'abc'  
    
    # NOTE:zhouf, 170315
    # 访问一个对象的属性的时候，这个函数是都会被调用用，也就是说， 这个是对象访问属性的机制决定的。 
    # 可以重写这个属性，就可以修改一些默认的行为，或是形成一个钩子，加入自己的一些东西。
    # 这个是新式类加入的一个属性。如果是旧式类是不会调用这个属性的。
    def __getattribute__(self, *args, **kwargs):  
        print("__getattribute__() is called"), args, kwargs  
        return object.__getattribute__(self, *args, **kwargs)  
        #return "haha"  
    
    # NOTE:zhouf, 170315
    # 这个属性不管是新式类，还是旧式类都会调用的。    
    def __getattr__(self, name):  
        print("__getattr__() is called ")  
        return name + " from getattr"  
      
    def __get__(self, instance, owner):  
        print("__get__() is called", instance, owner)  
        return self  
      
    def foo(self, x):  
        print(x)  

# d是描述符。        
class C2(object):  
    d = C()
    #d=2  

def func1():
    c = C()  
    c2 = C2()  
    print 'c.a:',(c.a)  
    print(c.zzzzzzzz)  
    # 
    print 'c2:', c2, c2.d#c2.d.foo(3)
    print c2.d
    print c2.d.x
    print '='*20
    class Desc(object):
        def __get__(self, obj, owner):
            return self
    d=Desc()        
    c.d=d   # 实例属性实现了__get__方法，在访问实例属性的时候不会调用__get__方法。
    print c.d

def func2():
    # 因为这是一个旧式类， 所以写了__getattr__之后就出现了很多错误。
    # 只有在新式类里面描述符特性才会起作用。且只有对象作为一个其他类的属性出现时，才会使用描述符特性
    class Dog(object):
    #class Dog():
        def __get__(self, ins, o):
            print 'sss'
            #return self
            return 45
        # 定义了这个属性之后， print h.d就会报错。
        def __getattr__(self, name):  
            print("__getattr__() is called ")  
            #return name + " from getattr"  
    d=Dog()
    # 在这里就会报错
    print 'd:1:', d #type(d)
    #
    class House(object):
        d=Dog()
    h=House()
    print 'House.__dict__:', House #House.__dict__
    print 'h.d:', h.d
    #h.d2=Dog()   #这个不算描述符。描述符必须是类的属性.
    House.d2=Dog()  #这是是描述符。
    print 'h.d2:', h.d2
    
    
# 类属性如果实现了__get__函数，在访问该属性时，会调用该属性的__get__方法。
if __name__ == '__main__':  
    func2()
    
    