#encoding:utf8

class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"
class B(A):
    def __init__(self):
        print "enter B"
        #super(B,self).__init__()   # 正确的
        #super(B,B).__init__()    #报错
        super(B).__init__(self)    #报错
        print "leave B"
def func1():
    b=B()

if __name__=="__main__":
    func1()