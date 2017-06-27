#!usr/bin/env python
#coding:utf-8

"""
测试Python函数是的参数是否有输出功能。
"""

import json
import sys

class Debug(object):
    def __init__(self):
        pass
    def trace(self, msg):
        print "trace:", msg
debug=Debug()

def func2(a):
    a.append(2)

# 用列表作为参数可以达到指针传递的效果    
def func1():
    debug.trace(["func1:start:"])
    a=[]
    func2(a)
    debug.trace(["a:", a])
    
        
if __name__ == "__main__":
    debug.trace(["sys.args:", sys.argv])
    tmpargv=sys.argv
    for item in tmpargv:
        #item=item.replace(r'\"', r'"')
        debug.trace(["type,len:", type(item), len(item), item])
    #func1()
    #func2()
    #func3()
    #func4()
