#!/usr/bin/env python
#encoding:utf-8

import os

total=0

r1,w1=os.pipe()  
r2,w2=os.pipe()

pid0=os.getpid()
print 'main process:',pid0

pid1=os.fork()

'''
print '测试',pid1               #为了演示os.fork()有两个返回值

#下面为了演示os.getpid()值不是固定的 其显示当前进程ID

if pid1==0:
    print '子进程 ',pid1,os.getpid(),os.getppid()
else:
    print '主进程 ',pid1,os.getpid(),os.getppid()
'''

if pid1  == 0:
    print 'this is child01' ,'子进程1',os.getpid()
   
    os.close(r1)
    fw01=os.fdopen(w1,'w')
    fw01.write('99')    

else :
    status1=os.waitpid(pid1,0)  
    pid2=os.fork()
    
    if pid2 == 0:
        print 'this is child02' ,'子进程2',os.getpid()
        os.close(r2)
        fw02=os.fdopen(w2,'w')
        fw02.write('100')          

    else :
        status2=os.waitpid(pid2,0)  
        print 'this is parent00','主进程',os.getpid(),'  its child01',pid1,' its child02',pid2
        os.close(w1)
        os.close(w2)
        fr001=os.fdopen(r1,'r')
        fr002=os.fdopen(r2,'r')
        add1=fr001.read()
        add2=fr002.read()
        total=total+int(add2)-int(add1)
        print 'total =',total