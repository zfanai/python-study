#!usr/bin/env python
# -*- coding: utf-8 -*

'''
1.
'''

#
class Debug(object):
    def __init__(self):
        pass
    def trace(self,msg):
        print "LanguageTest:", msg
debug=Debug()

#
class Animal(object):
    def __init__(self):
        pass

#
def func1():
    pass
    debug.trace(["func1:start:"])
    a=Animal()
    a.weight=10
    debug.trace(["func1:a.weight:", a.weight])
    #对象是没有get函数的，这个函数只有dict对象有，对象比字典好用，因为可以随意的用.操作符添加属性
    #debug.trace(["func1:a.color:", a.get(color,None)])
    #a["color"]=23    # 不支持
    debug.trace(["func1:a.dir:", dir(a)])
#
if __name__ == "__main__":
    debug.trace(["main:start:"])
    func1()
    
    