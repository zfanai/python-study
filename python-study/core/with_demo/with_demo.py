#!usr/bin/env python
# -*- coding: utf-8 -*

# in 关键字使用的是迭代器功能，只要对象实现了迭代器接口
# 就可以使用in关键字
class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def printraw(self, obj):
        pass
        print obj
debug=Debug()

def func2():
    f=open('123.txt')
    debug.trace('func2')
    
def func1():
    #c = C()
    #for a in c:
    #    debug.printraw(a)
    # with处理不了open出错的情况，但是可以处理read出错的情况。以及close()动作等清理工作
    #
    with open('123.txt') as f:
        print 'func1'
    print 'func1 2' 

class Sample(object):
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print "In __exit__()"
 
 
def get_sample():
    return Sample()
 
def func3(): 
    # 使用get_sample和Sample()的效果是一样的。
    #with get_sample() as sample:
    with Sample() as sample:        
        print "sample:", sample
     
if __name__ == '__main__':
    func3()