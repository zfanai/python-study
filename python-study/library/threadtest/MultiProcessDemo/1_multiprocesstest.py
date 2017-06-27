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
    # @zfn Pool()����������һ���̳߳ء�
    pool=multiprocessing.Pool()
    debug.trace(['func2.pool:', pool])
    # @zfn ������һ����ǰ�һ�δ��붪��һ���̳߳أ�����ȥ������ôִ�С�
    # ��δ��롣
    result = pool.apply_async(f, [10])
    debug.trace(['func2.result:', result])
    # @zfn ���ִ�еĽ��������timeout�����������timeoutָ����ʱ����û��
    # ִ����ɣ��ͻ᷵�ز�����TimeoutError�쳣��
    tmp1=result.get(timeout=1)
    debug.trace(['func2.tmp1:', tmp1])
    # @zfn map����ִ�ж��ʵ�����ȵ��ӽ��̶�ִ����ɲŻ᷵�أ�������һ������
    # ���ǣ��п����ֶ���ֹ�����̵�ʱ��������̾���Զ���޷���ֹ�ˡ�
    # ����һ�ַ�ʽ����map_async�ĵ��÷�ʽ�����������̵���֮������Ϸ��أ�Ȼ��ͨ��get����
    # ����ȡִ�еĽ����
    tmp2=pool.map(f, range(10))
    #
    debug.trace(['func2.tmp2:', tmp2])
def func1():
    #pool=multiprocessing.Pool(processes=2)
    # �����ָ��processes������Ĭ�ϵľ�������4�����̡�
    # pool�ͱ�ʾ���ǽ��̳ء�
    pool=multiprocessing.Pool()
    debug.trace(['pool:', dir(pool)])

if __name__=='__main__':
    #func1()
    func2()

debug.trace(['main:tp9,__name__,pid:', __name__, os.getpid()])    