#encoding:gbk
import matplotlib.pyplot as plt
import numpy as np

# ������Ļ�ͼ���ܡ�
def func1():
    plt.plot([1,2,3,4])
    plt.ylabel('Some numbers')
    plt.show()

# ����x,y������
def func2():
    plt.plot([1,2,3,4], [1,4,9,16])
    #plt.ylabel('Some numbers')
    plt.show()

# ������������
def func3():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0,6,0,20])
    plt.show()

# ʹ��numpy����
def func4():
    t=np.arange(0., 5., 0.2)
    # **����������š�t����������**�������
    plt.plot(t,t,'r--', t, t**2, 'bs', t,t**3, 'g^')
    plt.show()

# �����ߵ����ԡ�
def func5():
    pass
    # �鿴�ĵ���

# �����ͼ�����ӡ�    
def func6():
    def f(t):
        return np.exp(-t)*np.cos(2*np.pi*t) 
    t1=np.arange(0.0, 5.0, 0.1)
    t2=np.arange(0.0, 5.0, 0.02)
    plt.figure(1)
    plt.subplot(211)  # ����plt.subplot(2,1,1), ������˳��ֱ��������������� ��š�
    plt.plot(t1,f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

def func7():
    plt.figure(1)
    plt.subplot(211)
    plt.plot([1,2,3])
    plt.subplot(212)
    plt.plot([4,5,6])
    
    plt.figure(2)
    plt.plot([4,5,6])
    
    plt.figure(1)
    plt.subplot(211)
    plt.title('Easy as 1,2,3')
    plt.show()
    
def func8():
    mu, sigma = 100, 15
    x=mu+sigma*np.random.randn(10000)
    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    
    #
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40,160,0,0.03])
    plt.grid(True)
    plt.show()
    
def func9():
    ax=plt.subplot(111)
    t=np.arange(0.0, 5.0, 0.01)
    s=np.cos(2*np.pi*t)
    line,=plt.plot(t,s,lw=2)
    # ����д���Ļᱨ��
    plt.annotate('local max', xy=(2,1), xytext=(3,1.5), 
                arrowprops=dict(facecolor='black', shrink=0.05))
    plt.ylim(-2, 2)
    plt.show()
#
if __name__ == '__main__':
    func9()

