#encoding:gbk
import datetime

class Debug(object):
    def trace(self, msg):
        nt=datetime.datetime.now()
        print '[%s]:%s'%(nt.strftime('%Y%m%d%H%M%S'), msg)
debug=Debug()

# �ֵ���ô����
def test_func1():
    pass
    dicta={"a":1,"b":2}
    for k,v in dicta.items():
        print k
        print v 

class Base1(object):
    x=1
    y=2
# dict()�ǹ�������������һ���µ��ֵ����
# ���һ���ֵ�Ҫ�������������ʹ�����������
def test_func2():
    b=Base1()
    debug.trace(['dict(b)', dict([1,2])])
    
if __name__=="__main__":
    test_func2()