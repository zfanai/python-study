#encoding:gbk

#class C(object):
class C:
    def __init__(self):
        self.y=3
        pass
    
    """
    ��������ʽ�໹�Ǿ�ʽ�࣬�ڸ�ֵ��ʱ�򣬶�������������,����಻����ʽ�������
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