# encoding:gbk
import threading
import time
import sys

'''
问题产生的原因就是没有控制多个线程对同一资源的访问，对数据造成破坏，使得线程运行的结果不可预期。这种现象称为“线程不安全”。
互斥锁同步

上面的例子引出了多线程编程的最常见问题：数据共享。当多个线程都修改某一个共享数据的时候，需要进行同步控制。

线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。互斥锁为资源引入一个状态：锁定/非锁定。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
'''
class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        num = num+1
        msg = self.name+' set num to '+str(num)
        print msg
num = 0
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
    print 'end'
    sys.exit()