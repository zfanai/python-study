#encoding:gbk

import datetime

# ����ļ���__dict__��ص����ԡ�
class Debug(object):
    def trace(self,msg):
        nt=datetime.datetime.now()
        print "[%s]:%s" % (nt.strftime('%Y%m%d%H%M%S'), msg)
debug = Debug()

# __dict__������û����ô������ά��ʵ���ľֲ����ԡ�
class Base1(object):
    pass
    __dict__={}  # ֻ��Ӱ�쵽Base1���ʵ����__dict__���ԣ�Ӱ�첻��Base1���__dict__���ԡ�
    v__dict__={}
    @property
    def w__dict__(self):
        print 1
        return {}

def test_func1():
    b=Base1()
    b.x=2
    debug.trace(['b.x:', b.x])
    #b.__dict__()
    debug.trace(['b.__dict__:', b.__dict__, type(b.__dict__), dir(b)])
    debug.trace(['Base1.__dict__:', Base1.__dict__, Base1.v__dict__])
    
class Dog(object):
    pass

def func2():
    d=Dog()
    d.x=2
    # ʵ����__dict__�������ֵ�����
    print 'd.__dict__:', d.__dict__
    print 'type(d.__dict__):', type(d.__dict__)
    # ���__dict__������dictproxy����
    print 'Dog.__dict__:', Dog.__dict__
    print 'type(Dog.__dict__):', type(Dog.__dict__)
    print 'Dog.__dict__["__dict__"]:',  Dog.__dict__["__dict__"], type(Dog.__dict__["__dict__"])
    #print 'Dog.__dict__.__dict__:', Dog.__dict__.__dict__
    
    # ɾ���� d.__dict__���������x, Ҳ���൱��ɾ����d��x����
    del d.__dict__['x']
    print 'd.__dict__:', d.__dict__
    
    # ����__dict__��ֵ�൱�ڸ���d������
    d.__dict__={'a':1, 'b':2}
    print 'd.a,d.b:', d.a, d.b
    
    # ���__dict__�����ǲ����еģ� ǰ��Ĵ�ӡ��Ϣ����Dog.__dict__��һ�����ԣ� 
    #Dog.__dict__={'s':1, 'd':2}
    
def func3():
    # NOTE��zhouf, 170315, ���͵�__dict__���Ե�������dictproxy�� ��������ǲ���д��
    # ���԰�������Ե����ֵ����ã� ������ʵ�����ֵ�����. ����ֵ����__dict__�ֶΡ�
    print 'Dog.__dict__:', Dog.__dict__, type(Dog.__dict__)
    # NOTE�� zhouf, 170315, ����Զ�������������漰�� attribute�� type, class, object
    #  ������������ͣ� ���͵�����Ҳ�����ͣ� ���;�������֮ʼ�ˡ� attributeӦ����Python���Ե�һ���ڽ����
    print Dog.__dict__['__dict__'], type(Dog.__dict__['__dict__']), Dog, Dog()
    # NOTE��zhouf, 170315, ����������ᱨ��. ���͵�ʵ�����ࣩ��__dict__�����ǲ���д�ġ�
    #Dog.__dict__={}
    Dog.a=1
    d=Dog()
    print 'd.a:', d.a  # d��û��a������ԣ� ֮���Կ��Է���a������ԣ� ����Ϊd��Dog��ʵ����d�����Է��ʻ��ƾ�����
    # ���ϣ� d����û��������ԣ����Ǿ�������������ȥ����û��������ԡ�
    print 'd.__dict__:', d.__dict__

def func4():
    class Dog(object):
        def run(self):pass
    print 'Dog.__dict__:', Dog.__dict__    
    
    
if __name__ == "__main__":
    #test_func1()
    func4()
    
