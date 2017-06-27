#encoding:gbk

"""
property修改符的用法：
1.可以使用property修饰符
2.x.setter和x.deleter增加属性的设置和删除方法
3.新式类@property修饰的属性默认为read-only如果没有设置setter,就不能直接赋值
4.属性的读写权限可能是通过描述符来实现的,
"""

class Parrot(object):  
    def __init__(self):  
        self._voltage = 100000  
  
    @property  
    def voltage(self):  
        """Get the current voltage."""  
        return self._voltage  

def test_func1():
    pass
    # instance  
    p = Parrot()  
    # similarly invoke "getter" via @property  
    print p.voltage  
    # update, similarly invoke "setter"  
    p.voltage = 12
    
    
if __name__ == '__main__':
    test_func1()
    #test_func2()


