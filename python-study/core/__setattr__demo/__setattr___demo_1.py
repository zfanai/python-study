#encoding:gbk

#class C(object):
class C:
    def __init__(self):
        self.y=3
        pass
    
    """
    ��������ʽ�໹�Ǿ�ʽ�࣬�ڸ�ֵ��ʱ�򣬶�������������,����಻����ʽ�������
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
        # ����__xx��ʽ�ı�������˽�б���������ע��ĩβ��__�����ı������㡣
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
        # __setattr__�൱���ǵ�����������غ�����
        def __setattr__(self, name, val):
            print 'call __setattr__:', name
            #self.name=val   # ����д�ͻ�ѭ��Ƕ�׵���
            # ����self�ĵ����ֻ�Ƕ����ԣ� ���Բ������__setattr__������Ҳ�Ͳ������ѭ��Ƕ�׵�����
            self.__dict__[name]=val
    a=A()
    # ����ط��϶����ڲ����⴦�� __dict__���������ԣ���Ȼ����
    # ���ܸ�__dict__�������÷��ֵ����͵�ֵ��
    a.__dict__=2    # __dict__���ִ���
    #a.y=4
    #print 'a.y:', a.y
    a.x=2
    print a.__dict__
    a.__dict__['ss']=123
    print dir(a), type(a.__dict__), a.__dict__
    print type(a.__dict__), type(A.__dict__)
    A.__dict__=2   # ���޸����__dict__�ǲ����еġ��������ʵ������������ġ�
    
if __name__=="__main__":
    #test_func1()
    #func2()
    #func3()
    func4()