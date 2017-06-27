#encoding:gbk

# 旧式类， C的实例， 叫做这个类的实例。
# 新式类， C的实例， 叫做这个类的对象。

#class C(object):
class C:
    def __init__(self):
        self.y=3
        pass
    
    """
    不能是新式类还是旧式类，在赋值的时候，都会调用这个函数,这个类不是新式类的特性
    """
    def __setattr__(self,name,value):
        pass
        print "__setattr__:",name,value
    
    # 这个不是访问对象属性时调用的函数， 访问对象属性是调用的函数是__getattr__
    def __get__(self, name):
        pass
        print 'call __get__'
        
    

def test_func1():
    c=C()
    c.x=2  # 
    print c.x

# 旧式类， 解释器认为新定义了一种系统的类型。
# 新式类， 解释器认为创建了一个类型类的实例。
class OldDog():pass
class NewDog(object):pass

def func2():
    print 'OldDog:', OldDog
    print 'NewDog:', NewDog
    
if __name__=="__main__":
    pass
    test_func1()
    #rint c.x
    #func2()