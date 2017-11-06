#encoding:gbk

#class C(object):
class C:
    def __init__(self):
        self.y=3
        pass
    
    """
    不能是新式类还是旧式类，在赋值的时候，都会调用这个函数,这个类不是新式类的特性
    """
    def __setattr2__(self,name,value):
        pass
        print "__setattr__:",name,value
    

def test_func1():
    c=C()
    c.x=2  # 
    print c.x

def func2():
    class B(object):pass
    a=B()
    a.x=2  
    a.__setattr__('y', 2)
    print a.y
    setattr(a, 'y', 'y3')
    print a.y
    B.__setattr__(a, 'z', 3)
    print a.z
    setattr(B, 'z', 'z3')
    print a.z, B.z
    a=B()
    print a.z
    #

class Dog(object):
    def __init__(self):
        # 对以__xx形式的变量进行私有保护，但是注意末尾以__结束的变量不算。
        #object.__setattr__(self, '__color', 'red')
        self.__color='red'
        
        object.__setattr__(self, '__color__', 'black')
        #self.__color_d_='black'
        
    def get_color(self):
        print self.__color
    def get_color2(self):
        print self.__color__
        
def func3():
    d=Dog()
    d.get_color()
    d.get_color2()
    
def func4():
    class A(object):
        # __setattr__相当于是点操作符的重载函数。
        def __setattr__(self, name, val):
            print 'call __setattr__:', name
            #self.name=val   # 这样写就会循环嵌套调用
            # 这里self的点操作只是读属性， 所以不会调用__setattr__函数。也就不会出现循环嵌套的现象。
            self.__dict__[name]=val
    a=A()
    # 这个地方肯定是内部特殊处理， __dict__是特殊属性，虽然给它
    # 不能给__dict__属性设置非字典类型的值。
    a.__dict__=2    # __dict__会字串化
    #a.y=4
    #print 'a.y:', a.y
    a.x=2
    print a.__dict__
    a.__dict__['ss']=123
    print dir(a), type(a.__dict__), a.__dict__
    print type(a.__dict__), type(A.__dict__)
    A.__dict__=2   # 而修改类的__dict__是不运行的。所以类和实例还是有区别的。
    
if __name__=="__main__":
    #test_func1()
    #func2()
    #func3()
    func4()