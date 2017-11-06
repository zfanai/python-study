#encoding:gbk

import datetime

class Debug(object):
    def trace(self,msg):
        nt=datetime.datetime.now()
        print "[%s]:%s" % (nt.strftime('%Y%m%d%H%M%S'), msg)
debug = Debug()

"""
��������£�Python����̬�����ԣ��ȿ��Ը�ʵ�������ԣ�Ҳ���Ը�������ԣ�
��ʵ��������ֻ��ĳ��ʵ�������ã���������Կ��ԶԸ��������ʵ�������ã�
������ʱ��ϣ�����ư����Եķ�Χ���Ϳ���ʹ��__slots__���Զ�����Զ�̬�󶨵����Ե�Ԫ��
__slots__=("name","age")
��ʾֻ����̬��name���Ժ�age����

NOTE:170316, �������ʶ�ǲ��Եģ� ��������Ծ�ֻ�Ǹ������һ�����ԣ� �����Ǹ�������ʵ��������������ԣ�
ֻ�����ʵ�����Է���������ԣ�������û�ж���������Ե�����£�����ж�������Է��ʵ��ڲ�����ʵ�ֵģ����ʵ��û��ĳ�����ԣ���������������������ԡ���
"""
class Base1(object):
    v = 1
    def __init__(self):
        pass

def test_func1():
    b = Base1()
    print b.__dict__
    b.x = 2
    print b.__dict__

class Base2(object):
    __slots__ = ('y')
    v = 1
    a=2
    def __init__(self):
        pass

def test_func2():
    b = Base2()
    #print b.__dict__    #���ͻ�����ˣ�Base2�ඨ����__slots__���ԣ���û����__dict__����
    debug.trace(["dir(b):", dir(b)])
    debug.trace(["Base2.y:", type(Base2.y), Base2.y])    # y���Բ�֪����ʲô
    debug.trace(["b.a,Base2.a:", b.a,Base2.a])   # �����ԣ�ʵ�����඼���Է��ʡ�
    
    #b.x = 2              #error,���������µı���
    #print b.__dict__

# __dict__�����Ĭ���������ԣ�ÿһ������ʵ����ʱ������һ���ֵ䣬����������ʱ�����ֵ�����
# ����ֵ������__slots__���ڲ����û��ǹ�ᵽӰ��__dict__�����ϣ���Ϊ������__slot__���Է�
# ʵ����û����__dict__���ԣ�ʵ��֮���Կ���������������Ϊ__dict__�����������ã�������Python
# ���ڲ����ơ����������__slot__����������__dict__���Ժ�ʵ���Ϳ������������ˡ����ǣ�����
# ������__slots__���Բ��Ұ�����__dict__�������Ͳ�����__slots__������ʲô�����ء�������__slots__
# ���Եı�������__slots__���ԣ���������__weakref__���ԡ�
'''
__dict__�����Ĭ���������ԣ�ÿһ������ʵ����ʱ������һ���ֵ䣬����������ʱ�����ֵ�����
����ֵ ---- ��仰�ǲ��Եġ� (����������ʱ��ֻ�������������ԣ�ʵ�����Է��ʵ�����������������Է��ʻ��ƾ�����)

'''
class Base3(object):
    __slots__=('__sdf', 'y', '_y', '_x')   # ������__dict__����, û���»��ߵ����Ծ���ֻ�������ԡ�
    #__slots__=('__sdf', 'y', "__dict__")   # ������__dict__���ԾͿ���ʹ�������������
                        # __sdf���ԣ��������»��߿�ͷ�����Ի��Զ�����_ClaaNameǰ׺��
    y = 2
    v = 1
    def __init__(self):
        pass
    
    def setY(self, y):
        pass
        debug.trace(["setY:y:",y])
        #object.__setattr__(self, 'y', y) # ���ַ�ʽ����y������Ҳ�ǲ��е�
        #self.y=y    # �ᱨ�� y��ֻ�����ԡ�JavaScript���Ե����Ե��������ƣ�ֻ����ƽʱ�����õ���
        # ÿһ��������Ը�������ܶ�����ԣ� ÿ�������������������ԣ��ɶ�����д�ȣ���
        self._y=y
        self.__sdf=y
        #self.__x=y+1    # ͬ����������__x���ڲ�д�����ⲿд�ǲ�һ���ģ����ڲ�д���Զ��ļ���'_����'��ǰ׺
        #self._z=y
        
def test_func3():
    b = Base3()
    #print b.__dict__
    #b.x = 2   # ������__slots__�� û��x���ԣ� ���ܸ�������Ը�ֵ���ҵ������PythonĬ������¶�����õ��������ʱ��
    # ��������������û��������ԣ� �ͻ��������󴴽�һ�����ԡ��������������__slots__���ͻ�ı������ֹĬ�ϵ���Ϊ��
    # û�и�������󴴽����ԣ� Ҳ���ܸ�������Ը�ֵ�ˡ� 
    #b.y = 3   #read only, __slots__����������y, y�ͱ����ֻ�������ˡ�
    b.setY(4)
    debug.trace(["b.y:", b.y])
    debug.trace(["b._y:", b._y])
    debug.trace(["b.__sdf:", b._Base3__sdf])
    
    # 
    # ֻ��˫�»��߾�����������壬���»�����������ͨ���ַ���
    # �Ͼ�Ҳ�����⣬���»��ߵı����ǿ����޸ĵģ������»��ߵ�
    # ������ֻ��������(���������__slots__)�����ܸ�ֵ��
    b._x=2  #
    debug.trace(["b._x:", b._x])
    #b.a=123
    
    #b.y=3
    #debug.trace(["b.y:", b.y])   
    
    debug.trace(["dir(b):", dir(b)])
    
"""

"""
class LocalProxy(object):
    __slots__ = ('__local', '__dict__', '__name__', 'dfg') # ���ﶨ��ľ���������

    def __init__(self, local, name=None):
        pass
        object.__setattr__(self, '_LocalProxy__local', local)
        #object.__setattr__(self, '_LocalProxy__locael', local)
        #object.__setattr__(self, '__name__', name)

    def _get_current_object(self):
        pass
        debug.trace([ "_get_current_object"])
        debug.trace([ "self.__local", self.__local])
        #print dir(self)
        #print dir(LocalProxy)
        #print self.__name__
        
        #if not hasattr(self.__local, '__release_local__'):
        #    return self.__local()
        #try:
        #    return getattr(self.__local, self.__name__)
        #except AttributeError:
        #    raise RuntimeError('no object bound to %s' % self.__name__)

def test_func4():
    proxy=LocalProxy("local-val2", "local-name")
    proxy._get_current_object()
    proxy.__localw = "sdf"
    
    #print dir(proxy)  # ʵ������
    #print dir(LocalProxy) #������
    #print proxy.__localw
    #print proxy._LocalProxy__local
    debug.trace(["dir(proxy)", dir(proxy)])   # ʵ������
    debug.trace(["dir(LocalProxy)", dir(LocalProxy)]) #������
    debug.trace(["proxy.__localw", proxy.__localw])
    debug.trace(["proxy._LocalProxy__local", proxy._LocalProxy__local])
    #print proxy.__local      # ���ⲿ����������˫���߿�ͷ�����ԣ���Ϊ�������Ѿ����滻��һ�����������,������_ClassNameǰ׺

class Animal(object):
    pass

def test_func5():
    a=Animal()
    # ʵ��û��__name__���ԣ��������д����ԡ�
    #debug.trace(['__name__:', a.__name__])
    debug.trace(['__name__:', Animal.__name__])

def func6():
    class Dog(object):
        a=1
    d=Dog()
    print 'getattr:', getattr(d, 'a')
    print 'hasattr:', hasattr(d, 'a')
    Dog.b=3
    print 'dir(d):', dir(d)   #�г�����d���ʵ�����Է��ʵ��Ķ���
    print 'd.__dict__:', d.__dict__
    
if __name__ == "__main__":
    #test_func1()
    #test_func2()
    test_func3()
    #test_func4()
    #test_func5()
    #func6()
    
