#encoding:gbk

import sys
from datetime import *
import subprocess

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1(pwd, db, of):
    n=datetime.now()
    #args=['mysqldump', '-uroot',  '-pmtdb027471TA', 'flaskdb']
    args=['mysqldump', '-uroot',  '-p'+pwd, db]
    #args=['mysqldump', '-uroot',  '-pmyzfsql85', 'test']
    debug.trace(['args:', args])
    #fnm='flaskdb_%s.sql' % n.strftime('%Y%m%d%H%M%S')
    fnm = of
    fo=open(fnm, 'w')
    p=subprocess.Popen(args, shell=True, stdout=fo)
    #p=subprocess.Popen(args, shell=True)
    debug.trace(['p:', p])
    p.wait()
    debug.trace(['p.wait finish:'])
    p.terminate()
if __name__=='__main__':
    if len(sys.argv)!=4:
        debug.trace(['args is not right.'])
    #
    pwd=sys.argv[1]
    db=sys.argv[2]
    of=sys.argv[3]
    debug.trace(['pwd,db,of:', pwd,db,of])
    func1(pwd, db, of)

