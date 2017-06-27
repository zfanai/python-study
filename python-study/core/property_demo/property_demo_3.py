#encoding:gbk

"""
property修改符的用法：
1.可以使用property修饰符
2.x.setter和x.deleter增加属性的设置和删除方法
"""

# Python不支持函数重载，但是定义两个函数不会报错。后面定义的函数会覆盖前面定义的函数。
class Dog(object):
    def run(self):pass
    def run(self,speed):pass

class C(object): 
#class C: 
    def __init__(self): 
        self.__x=None 
        
    #下面就开始定义属性了 , property修饰符会把被修饰的函数变成一个属性。
    @property 
    def x(self): 
        print 'in x:'
        return self.__x 
    '''
    123
    '''
    # x是一个property对象。
    #print x,type(x),dir(x)
    # 下面的setter和deleter好像没起作用。在旧式类里面不起作用，但是在新式类里面
    # 会起作用。
    @x.setter   
    def x(self,value):
        print 'setter:'
        self.__x=value + 1
        
    @x.deleter 
    def x(self): 
        del self.__x 

def test_func1():
    pass
    c=C()
    print 'c.x:1:', c.x
    c.x=100
    print 'c.x:2:', c.x
    y=c.x
    print 'y:', y
    del c.x

def test_func2():
    d=Dog()
    d.run()
    d.run(2)

    
if __name__ == '__main__':
    test_func1()
    #test_func2()


