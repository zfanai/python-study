#encoding:gbk

import sys

# raise string����ʽ�Ѿ���ʱ������֧��
def test_func1():
    pass
    try:
        print "start"
        raise "raise except"   # ��ʵ���ǳ���һ��TypeError, ����һ�䱾���׳����쳣��Ҳ����˵���쳣�Ĺ����з������쳣��
    except Exception,e:
        print "001:", "catch except"
        print "002:", e
        print "003:", type(e)
        print "004:", dir(e)
        print "005:", e.message
        print "006:", e.args
        #print 

def test_func2():
    pass
    try:
        print "start"
        raise Exception, "args"  # args���쳣����Ϣ
    except Exception,e:
        print "001:", e
        print "002:", type(e)
        print "003:", dir(e)
        #print (sys.exc_info())[2]

if __name__=="__main__":
    #test_func1()
    test_func2()
    