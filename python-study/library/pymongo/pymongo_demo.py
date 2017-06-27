#encoding:gbk
import os
from zftrace import debug
import functools 
import pymongo

debug.trace=functools.partial(debug.trace, 'app')

def func1():
    comm=pymongo.Connection('localhost', 27017)
    db=conn.ChatRoom
    account=db.Account
    
if __name__=='__main__':
    func1()