#encoding:gbk
from greenlet import greenlet

# greenlet的最基本的应用就是switch函数，可以在两个执行体之间跳来跳去
def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
# 转向gr1进行执行,开始的时候gr1还没有开始执行
gr1.switch()

