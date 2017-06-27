#!usr/bin/env python
# -*- coding: utf-8 -*

class Debug(object):
    def trace(self, msg):
        print "trace:", msg
debug=Debug()

def fab1(max):
    n,a,b = 0, 0, 1
    while n < max:
        print b
        a , b = b, a + b
        n = n + 1

def fab2(max):
    n,a,b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a , b = b, a + b
        n = n + 1
    return L
    
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

def func1():
    pass
    
# 函数体里面包含yield语句，函数跟普通的函数行为就不一样了，
# 这个函数就变成了一个生成器。在调用这个函数是fn(x)只是生成了
# 一个生成器对象，函数体里面的代码并不会执行。
def fab3(max):
    debug.trace(["fab3:start:"])
    
    n,a,b = 0, 0, 1
    while n < max:
        yield b
        #print b
        a , b = b, a + b
        n = n + 1

def func2():
    #fab1(5);
    tmp=fab3(5)   # 生成器只有在迭代环境里面才会真正的执行里面的代码。
    debug.trace(["tmp:", tmp, fab3])
    #
    for n in fab3(5):
        print n

class Dog(object):
    def __init__(self,a):
        self.a=a

def wrap(f):
    def aa():
        f()
    return aa

#@wrap    
def func3():
    debug.trace(['func3 start'])
    a=1
    for i in xrange(5):
        ret=yield Dog(a)
        a += 1
    
def func4():
    d=func3()
    debug.trace(['func4 start'])
    #for item in d:debug.trace(['d:', item, item.a])    

def func5():
    def func5_2():
        #for i in xrange(3):yield i*2
        return i
    # 
    def func5_1():
        debug.trace(['func5_1 start'])
        a=1
        # yield表达式的返回值是生成器调用send函数是传递的参数。
        for i in xrange(5):
            ret=yield func5_2()
            debug.trace(['ret:', ret])
            a += 1
    d=func5_1()
    for item in d:debug.trace(['d:', item])    
      
def func6():
    def func6_1():
        for i in xrange(5):
            yield i
    g=func6_1()
    print next(g)
    print next(g)
    print list(g)   # 关于迭代的用法。
 
if __name__ == '__main__':
    func6()