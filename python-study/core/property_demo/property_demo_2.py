#encoding:gbk

"""
property修改符的用法：
1.
"""



class C:
    """
            用的是旧式类
    """
    def __init__(self): 
        self.__x=None 
        
    #1.现在介绍第一种使用属性的方法： 
    #在该类中定义三个函数，分别用作赋值、取值和删除变量（此处表达也许不很清晰，请看示例） 
    def getx(self): 
        return self.__x 
    
    def setx(self,value): 
        self.__x=value 
    
    def delx(self): 
        del self.__x 
    
    # 生成了一个属性    
    x=property(getx,setx,delx,'') 


def test_func1():
    pass
    c=C()
    c.x=100
    y=c.x
    print y
    del c.x

def test_func2():
    pass

    
if __name__ == '__main__':
    test_func1()
    #test_func2()


