#encoding:gbk
'''
2016-8-1 getattr�Ǻ��������Ի��ĳ����������ԣ�__getattr__�����غ���
�ڶ����������ʱ�����á�
'''
class C():
#class C(object):  
    a = 'abc'  
    
    # NOTE:zhouf, 170315
    # ����һ����������Ե�ʱ����������Ƕ��ᱻ�����ã�Ҳ����˵�� ����Ƕ���������ԵĻ��ƾ����ġ� 
    # ������д������ԣ��Ϳ����޸�һЩĬ�ϵ���Ϊ�������γ�һ�����ӣ������Լ���һЩ������
    # �������ʽ������һ�����ԡ�����Ǿ�ʽ���ǲ������������Եġ�
    def __getattribute__(self, *args, **kwargs):  
        print("__getattribute__() is called"), args, kwargs  
        return object.__getattribute__(self, *args, **kwargs)  
        #return "haha"  
    
    # NOTE:zhouf, 170315
    # ������Բ�������ʽ�࣬���Ǿ�ʽ�඼����õġ�    
    def __getattr__(self, name):  
        print("__getattr__() is called ")  
        return name + " from getattr"  
      
    def __get__(self, instance, owner):  
        print("__get__() is called", instance, owner)  
        return self  
      
    def foo(self, x):  
        print(x)  

# d����������        
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
    c.d=d   # ʵ������ʵ����__get__�������ڷ���ʵ�����Ե�ʱ�򲻻����__get__������
    print c.d

def func2():
    # ��Ϊ����һ����ʽ�࣬ ����д��__getattr__֮��ͳ����˺ܶ����
    # ֻ������ʽ���������������ԲŻ������á���ֻ�ж�����Ϊһ������������Գ���ʱ���Ż�ʹ������������
    class Dog(object):
    #class Dog():
        def __get__(self, ins, o):
            print 'sss'
            #return self
            return 45
        # �������������֮�� print h.d�ͻᱨ��
        def __getattr__(self, name):  
            print("__getattr__() is called ")  
            #return name + " from getattr"  
    d=Dog()
    # ������ͻᱨ��
    print 'd:1:', d #type(d)
    #
    class House(object):
        d=Dog()
    h=House()
    print 'House.__dict__:', House #House.__dict__
    print 'h.d:', h.d
    #h.d2=Dog()   #����������������������������������.
    House.d2=Dog()  #��������������
    print 'h.d2:', h.d2
    
    
# ���������ʵ����__get__�������ڷ��ʸ�����ʱ������ø����Ե�__get__������
if __name__ == '__main__':  
    func2()
    
    