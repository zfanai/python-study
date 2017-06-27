#encoding:gbk

g=2

print 'module2 global code.tp0'
import module3
print 'module2 global code.'

def func1():
    global g
    print 'module2.func1'
    g += 1
    print 'module2.g:', g