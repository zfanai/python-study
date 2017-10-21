#encoding:utf8

import numpy as np

def func1():
    a=np.random.random((2,3))
    print 'f1:1.1:', a, type(a)
    b=a
    print 'f1:1.2:', b

    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    print 'f12:', x, type(x)
    x = np.atleast_2d(x)
    #x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    print 'f13:', x, type(x)
    
    # 矩阵
    y = np.array([[0, 0, 1, 1]]).T
    print 'f14:', y
    
    d=np.dot(10, 23)
    print 'f15:', d

    a = np.random.random((3))
    print 'f16:', a
    b=np.tanh(a)
    print 'f17:', b

    a0 = np.array([1, 2])
    a1=np.array([1,2,3])
    a2 = np.array([4, 5, 6])
    a3 = np.array([[4, 5, 6], [4, 5, 7]])
    print 'f18:', a1,a2, a1*a2
    print 'f19:', a1, a3, a1*a3
    print 'f20:', np.dot(a1, a3)
    
if __name__=="__main__":
    func1()