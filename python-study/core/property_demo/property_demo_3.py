#encoding:gbk

"""
property�޸ķ����÷���
1.����ʹ��property���η�
2.x.setter��x.deleter�������Ե����ú�ɾ������
"""

# Python��֧�ֺ������أ����Ƕ��������������ᱨ�����涨��ĺ����Ḳ��ǰ�涨��ĺ�����
class Dog(object):
    def run(self):pass
    def run(self,speed):pass

class C(object): 
#class C: 
    def __init__(self): 
        self.__x=None 
        
    #����Ϳ�ʼ���������� , property���η���ѱ����εĺ������һ�����ԡ�
    @property 
    def x(self): 
        print 'in x:'
        return self.__x 
    '''
    123
    '''
    # x��һ��property����
    #print x,type(x),dir(x)
    # �����setter��deleter����û�����á��ھ�ʽ�����治�����ã���������ʽ������
    # �������á�
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


