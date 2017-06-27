#encoding:utf8

class DistanceForm(object):
    def __init__(self, origin):
        self.origin = origin
        print "origin :"+str(origin)
    def __call__(self, x):
        print "x :"+str(x)

def func1():
    p = DistanceForm(10)
    p(20)   # 对象可调用
    print type(p),type(DistanceForm)

if __name__ == "__main__":
    print "call demo"
    func1()
