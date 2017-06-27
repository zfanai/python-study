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

class C(object):
    def method1():
        pass
    
        
def func1():
    c = C()
    for a in c:
        debug.printraw(a)

if __name__ == '__main__':
    func1()