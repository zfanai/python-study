#encoding:gbk
'''
可以看到，加入互斥锁后，运行结果与预期相符。
同步阻塞

当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“同步阻塞”（参见多线程的基本概念）。

直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

'''
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num 
        time.sleep(1)

        if mutex.acquire(1):  
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.release()
num = 0
mutex = threading.Lock()
#mutex.acquire()

def func1():
    mutex.acquire()
    print 'func1.tp0'
    
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    func1()