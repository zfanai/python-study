#encoding:gbk

from datetime import *
import subprocess

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    n=datetime.now()
    #args=['mysqldump', '-uroot',  '-pmtdb027471TA', 'flaskdb']
    args=['mysqldump', '-uroot',  '-pmyzfsql85', 'flaskdb']
    fnm='flaskdb_%s.sql' % n.strftime('%Y%m%d%H%M%S')
    fo=open(fnm, 'w')
    p=subprocess.Popen(args, shell=True, stdout=fo)
    debug.trace(['p:', p])
    p.wait()
    debug.trace(['p.wait finish:'])
    p.terminate()
if __name__=='__main__':
    func1()

