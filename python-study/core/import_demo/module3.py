#encoding:gbk

print 'module3 global code.tp0'

import module2

g=2

print 'module3 global code.'

def func1():
    global g
    print 'module3.func1'
    g += 1
    print 'module3.g:', g
    module2.func1()