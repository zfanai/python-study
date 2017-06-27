#!/usr/bin/env python
#encoding:utf8
import socket
import threading
from time import sleep, ctime
import gevent
from gevent.queue import Queue, Empty
#from Queue import Queue



'''
1.把可调用执行类对象来作为执行体。
2.用gevent的Queue就要用gevent的并发执行方式。
  用多线程就应该用多线程的Queue。
'''

loops = [ 4, 2 ]
q=Queue()

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop1(nloop, nsec):
    '''print 'start loop1', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop1', nloop, 'done at:', ctime()'''
    try:
        msg=q.get(timeout=10)
        print 'get a msg:', msg
    except Empty:
        print 'queue is empty'

def loop2(nloop, nsec):
    '''print 'start loop2', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop2', nloop, 'done at:', ctime()   '''
    print 'put a msg'
    #q.put_nowait('msg #0')
    q.put_nowait('msg #0')

exe_func=[loop1, loop2]
def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:    # create all threads
        loop=exe_func[i]
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]),
            loop.__name__))
        threads.append(t)

    for i in nloops:    # start all threads
        threads[i].start()

    for i in nloops:    # wait for completion
        threads[i].join()

    print 'all DONE at:', ctime()

def main1():
    threads = [gevent.spawn(exe_func[i], i, loops[i]) for i in xrange(2)]
    r=gevent.joinall(threads)  
    #print r
    
if __name__ == '__main__':
    main1()
