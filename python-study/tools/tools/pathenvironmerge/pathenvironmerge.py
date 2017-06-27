#encoding:utf8
import sys
import os

class Debug(object):
    def trace(self, msg):
        print "trace:", msg
    def rprint(self, msg):
        print msg
        
debug=Debug()

def func1():
    for p in ["userpath.txt", "syspath.txt"]:
        f1=open(p)
        tmp=f1.readline()
        userpaths=tmp.split(";")
        f1.close()
        #debug.trace(tmp)
        #debug.trace(userpaths)
        for item in userpaths:
            debug.rprint(item)
        debug.rprint("\n")
    #
    

def func2():
    env=os.environ.keys()
    debug.trace(["env", env])

def func3():
    debug.rprint("====================================\n")
    
    path=os.environ['PATH']
    paths=path.split(";")
    debug.trace(["num", len(paths)])
    for item in paths:
        debug.rprint(item)
        #debug.rprint(v)
    
if __name__=='__main__':
    func1()
    func2()
    func3()
    