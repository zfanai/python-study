#encoding:gbk

# ��ʽ�࣬ C��ʵ���� ����������ʵ����
# ��ʽ�࣬ C��ʵ���� ���������Ķ���

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
    
    # ������Ƿ��ʶ�������ʱ���õĺ����� ���ʶ��������ǵ��õĺ�����__getattr__
    def __get__(self, name):
        pass
        print 'call __get__'
        
    

def test_func1():
    c=C()
    c.x=2  # 
    print c.x

# ��ʽ�࣬ ��������Ϊ�¶�����һ��ϵͳ�����͡�
# ��ʽ�࣬ ��������Ϊ������һ���������ʵ����
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