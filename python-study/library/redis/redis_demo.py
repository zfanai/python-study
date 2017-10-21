#encoding:gbk
import os
from zftrace import debug
import functools 
import redis

debug.trace=functools.partial(debug.trace, 'app')


def func1():
    r=redis.Redis(host='localhost', port=6379,db=0)
    r.set('guo', 'shuai')
    v=r.get('guo')
    debug.trace(v)
    v = r.get('user_type_613')
    print v
    
if __name__=='__main__':
    func1()