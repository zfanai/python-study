#encoding:gbk

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
    

def test_func1():
    c=C()
    c.x=2  # 
    print c.x
    
if __name__=="__main__":
    pass
    test_func1()
    #rint c.x