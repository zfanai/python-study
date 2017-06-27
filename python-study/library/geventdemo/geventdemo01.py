#!/usr/bin/env python
#encoding:utf-8
import socket   # 不导入这个包就会报  (libev) select unkown error的错误
import gevent
import random
import time

def task(pid):
    """
    some non-deterministic task
    """    
    #gevent.sleep(random.randint(0, 2)*0.001)
    print 'Task %s start:%s' % (pid, time.time())
    sec=random.randint(0, 3)
    gevent.sleep(sec)
    print 'Task %s done:%s,%d' % (pid, time.time(), sec)

def synchronous():
    for i in range(1, 10):
        task(i)
 
def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asynchronous()
                