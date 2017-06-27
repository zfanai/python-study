#encoding:gbk
import os
from zftrace import debug
import functools 
debug.trace=functools.partial(debug.trace, 'app')

def func1():
    pass
    
if __name__=='__main__':
    func1()