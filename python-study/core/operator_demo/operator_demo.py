#encoding:utf8
from zftrace import debug

def func1():
    class Dog(object):
        # __getitem__重载[]操作符
        def __getitem__(self,index):
            debug.trace('app', '__getitem__', index)
            #return 'a'
            return 'abc'[index]
    d=Dog()
    debug.trace('app', d[4])
    
if __name__=='__main__':
    func1()
