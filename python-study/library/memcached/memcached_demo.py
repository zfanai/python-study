#encoding:gbk
import os
from zftrace import debug
import memcache,time
import functools

debug.trace=functools.partial(debug.trace, 'app')

def func1():
    mc=memcache.Client(['127.0.0.1:11211'], debug=0)
    mc.set('name1', 'rose')
    v=mc.get('name1')
    debug.trace(v)
    
if __name__=='__main__':
    func1()