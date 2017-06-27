#encoding:gbk

print 'sdf'
#
from pylab import *
import matplotlib.pyplot as plt

def func1():
    print 'sdf'
    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    #print 'sdf'
    C,S = np.cos(X), np.sin(X)
    #print dir(C),C
    plot(X,C)
    plot(X,S)
    show()

def fun2():
    plt.plot([1,2,3])
    #plt.show()
    print plt
    #print dir(plt)
    #plt.show()
    # 保存图片错误。
    plt.savefig('test1.png', dpi=120)

if __name__=='__main__':
    func1()

