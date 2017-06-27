#!/usr/bin/env python

import thread
from time import sleep, ctime

"""
这种最简单的使用方式有一个问题，当主线程启动子线程完成后就退出了，但是子线程还没有结束，
子线程运行就会报错。所以在主线程里面增加了sleep指令来保证子线程运行结束。
"""

def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()

def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()

def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
