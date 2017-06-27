#encoding:gbk
from datetime import *
import multiprocessing
import os

class Debug(object):
    def trace(self, msg):
        n=datetime.now()
        print 'trace:', msg
        self.saveLog('[%s]trace:%s\n' % (n.strftime('%Y-%m-%d %H:%M:%S.%f'), msg))
    def saveLog(self, msg):
        n=datetime.now()
        name='log/log_%s_%d.txt' %(n.strftime('%Y%m%d'), os.getpid())
        fo=open(name, "a")
        fo.write(msg)
        fo.close
debug=Debug()

debug.trace(['main:tp0,__name__,pid:', __name__, os.getpid()])

def f(x):
    debug.trace(['function f:x:', x])
    return x*x

def func2():
    # @zfn Pool()函数创建了一个线程池。
    pool=multiprocessing.Pool()
    debug.trace(['func2.pool:', pool])
    # @zfn 下面这一句就是把一段代码丢给一个线程池，由它去安排怎么执行、
    # 这段代码。
    result = pool.apply_async(f, [10])
    debug.trace(['func2.result:', result])
    # @zfn 获得执行的结果，设置timeout参数，如果在timeout指定的时间内没有
    # 执行完成，就会返回并处罚TimeoutError异常。
    tmp1=result.get(timeout=1)
    debug.trace(['func2.tmp1:', tmp1])
    # @zfn map可以执行多个实例，等到子进程都执行完成才会返回，但是有一个问题
    # 就是，有可能手动终止主进程的时候，这个进程就永远都无法终止了。
    # 还有一种方式就是map_async的调用方式，这样主进程调用之后会马上返回，然后通过get函数
    # 来获取执行的结果。
    tmp2=pool.map(f, range(10))
    #
    debug.trace(['func2.tmp2:', tmp2])
def func1():
    #pool=multiprocessing.Pool(processes=2)
    # 如果不指定processes参数，默认的就是启动4个进程。
    # pool就表示的是进程池。
    pool=multiprocessing.Pool()
    debug.trace(['pool:', dir(pool)])

if __name__=='__main__':
    #func1()
    func2()

debug.trace(['main:tp9,__name__,pid:', __name__, os.getpid()])    