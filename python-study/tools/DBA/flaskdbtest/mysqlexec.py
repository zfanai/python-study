#encoding:gbk

from datetime import *
import subprocess
import sys

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

# @zfn 
def func1(pwd, db, sqlf):
    n=datetime.now()
    #args=['mysql', '-uroot',  '-pmtdb027471TA', 'flaskdbV0178']
    args=['mysql', '-uroot',  '-p'+pwd, db]
    #fnm='flaskdb_%s.sql' % n.strftime('%Y%m%d%H%M%S')
    
    fo=open(sqlf, 'r')
    p=subprocess.Popen(args, shell=True, stdin=fo)
    debug.trace(['p:', p])
    p.wait()
    debug.trace(['p.wait finish:'])
    p.terminate()
    fo.close()
    
if __name__=='__main__':
    if len(sys.argv) != 4:
        debug.trace(['args not right.'])
        sys.exit(1)
    # 
    pwd=sys.argv[1]
    db=sys.argv[2]
    sqlf=sys.argv[3]
    
    # 
    func1(pwd, db, sqlf)
