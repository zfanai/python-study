#encoding:gbk

import sys

# raise string的形式已经过时，不在支持
def test_func1():
    pass
    try:
        print "start"
        raise "raise except"   # 其实还是出发一个TypeError, 是这一句本身抛出的异常，也就是说抛异常的过程中发生了异常。
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
        raise Exception, "args"  # args是异常的信息
    except Exception,e:
        print "001:", e
        print "002:", type(e)
        print "003:", dir(e)
        #print (sys.exc_info())[2]

if __name__=="__main__":
    #test_func1()
    test_func2()
    