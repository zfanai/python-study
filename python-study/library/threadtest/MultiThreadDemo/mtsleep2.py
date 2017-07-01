#!/usr/bin/env python
#encoding:utf8

import thread
from time import sleep, ctime

"""
为了解决主线程退出，子线程还没有结束的情况，通过线程锁来同步。
"""

loops = [4, 2, 6, 3]

def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'starting threads...'
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, 
            (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
