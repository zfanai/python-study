#encoding:gbk
import datetime

class Debug(object):
    def trace(self, msg):
        nt=datetime.datetime.now()
        print '[%s]:%s'%(nt.strftime('%Y%m%d%H%M%S'), msg)
debug=Debug()

# 字典怎么遍历
def test_func1():
    pass
    dicta={"a":1,"b":2}
    for k,v in dicta.items():
        print k
        print v 

class Base1(object):
    x=1
    y=2
# dict()是工厂函数，生成一个新的字典对象。
# 如果一个字典要进行深拷贝，可以使用这个函数。
def test_func2():
    b=Base1()
    debug.trace(['dict(b)', dict([1,2])])
    
if __name__=="__main__":
    test_func2()