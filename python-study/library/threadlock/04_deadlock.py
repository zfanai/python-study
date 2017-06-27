#encoding:gbk

import threading
import time

'''
此时进程已经死掉。
可重入锁

更简单的死锁情况是一个线程“迭代”请求同一个资源，直接就会造成死锁：
复制代码
'''
class MyThread(threading.Thread):
    def run(self):
        global num 
        time.sleep(1)

        if mutex.acquire(1):  
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.acquire()
            mutex.release()
            mutex.release()
num = 0
mutex = threading.Lock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()