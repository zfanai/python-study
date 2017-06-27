#encoding=gbk

import sys
import os
import fnmatch
import traceback
import re
import shutil
import random
import datetime

class Debug(object):
    def trace(self, obj):
        print "trace:%s" % obj
    # @note python 不支持重载.
    def t(self, tag, msg):
        print "trace:%s,%s" % (tag, msg)
    def printraw(self, obj):
        print obj
debug=Debug()

def timeDura(h=0, m=0, s=0, d=0):
    return h*3600+m*60+s+d*(24*3600)

def dumpBasalRecord(basalRecord):
    strRes=''
    tmpRecord=map(lambda x:'%s,%s,%d,%s,%.4f'%(x[0].strftime('%Y-%m-%d %H:%M:%S'), 
                                               x[1],x[2],x[3].strftime('%Y-%m-%d %H:%M:%S'),
                                               x[4]), basalRecord)
    strRes='\n'.join(tmpRecord)
    return strRes

def dumpBolusRecord(bolusRecord):
    strRes=''
    tmpRecord=map(lambda x:'%s,%s,%.2f,%.2f'%(x[0].strftime('%Y-%m-%d %H:%M:%S'), 
                                              x[1],x[2],x[3]), bolusRecord)
    strRes='\n'.join(tmpRecord)
    return strRes

def getBasalRecord(no):
    basalRecord=[]
    #
    t=datetime.datetime(2016, 6, 19, 8, 13, 0)
    basalRecord.append([t, 'NEW', 0, t, 0])
    #
    st=datetime.datetime(2016, 6, 19, 8, 13, 10)
    dura=timeDura(8,36)
    et=st+datetime.timedelta(seconds=dura)
    basalRecord.append([st, 'BAS', dura, et, 1.2])
    #
    st=et
    dura=timeDura(14,24)
    et=st+datetime.timedelta(seconds=dura)
    basalRecord.append([st, 'BAS', dura, et, 1.8])
    #
    st=et
    dura=timeDura(20, 45)
    et=st+datetime.timedelta(seconds=dura)
    basalRecord.append([st, 'BAS', dura, et, 1.4])
    #
    st=et
    dura=timeDura(10, 20)
    et=st+datetime.timedelta(seconds=dura)
    basalRecord.append([st, 'BAS', dura, et, 0.8])
    #
    st=et
    dura=timeDura(22, 50)
    et=st+datetime.timedelta(seconds=dura)
    basalRecord.append([st, 'BAS', dura, et, 1.0])
    #
    st=et+datetime.timedelta(seconds=10)
    basalRecord.append([st, 'ENDM', 0, st, 0])
    
    basalRecord1=[
        [datetime.datetime(2016,6,21,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,21,4,0), 0.5],
        [datetime.datetime(2016,6,21,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,21,21,0), 1],
        [datetime.datetime(2016,6,21,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,22,0,0), 0.5],
        
        [datetime.datetime(2016,6,22,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,22,4,0), 0.5],
        [datetime.datetime(2016,6,22,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,22,21,0), 1],
        [datetime.datetime(2016,6,22,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,23,0,0), 0.5],
        
        [datetime.datetime(2016,6,23,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,23,4,0), 0.5],
        [datetime.datetime(2016,6,23,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,23,21,0), 1],
        [datetime.datetime(2016,6,23,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,24,0,0), 0.5],
        
        [datetime.datetime(2016,6,24,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,24,4,0), 0.5],
        [datetime.datetime(2016,6,24,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,24,21,0), 1],
        [datetime.datetime(2016,6,24,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,25,0,0), 0.5],
        
        [datetime.datetime(2016,6,25,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,25,4,0), 0.5],
        [datetime.datetime(2016,6,25,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,25,21,0), 1],
        [datetime.datetime(2016,6,25,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,26,0,0), 0.5],
        
        [datetime.datetime(2016,6,26,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,26,4,0), 0.5],
        [datetime.datetime(2016,6,26,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,26,21,0), 1],
        [datetime.datetime(2016,6,26,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,27,0,0), 0.5],
        
        [datetime.datetime(2016,6,27,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,27,4,0), 0.5],
        [datetime.datetime(2016,6,27,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,27,21,0), 1],
        [datetime.datetime(2016,6,27,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,28,0,0), 0.5],]
    
    basalRecord2=[
        [datetime.datetime(2016,6,21,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,21,4,0), 0.7],
        [datetime.datetime(2016,6,21,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,21,21,0), 1.2],
        [datetime.datetime(2016,6,21,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,22,0,0), 0.7],
        
        [datetime.datetime(2016,6,22,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,22,4,0), 0.7],
        [datetime.datetime(2016,6,22,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,22,21,0), 1.4],
        [datetime.datetime(2016,6,22,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,23,0,0), 0.7],
        
        [datetime.datetime(2016,6,23,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,23,4,0), 0.8],
        [datetime.datetime(2016,6,23,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,23,21,0), 1.4],
        [datetime.datetime(2016,6,23,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,24,0,0), 0.9],
        
        [datetime.datetime(2016,6,24,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,24,4,0), 0.8],
        [datetime.datetime(2016,6,24,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,24,21,0), 1.5],
        [datetime.datetime(2016,6,24,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,25,0,0), 0.9],
        
        [datetime.datetime(2016,6,25,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,25,4,0), 0.8],
        [datetime.datetime(2016,6,25,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,25,21,0), 1.5],
        [datetime.datetime(2016,6,25,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,26,0,0), 0.9],
        
        [datetime.datetime(2016,6,26,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,26,4,0), 0.8],
        [datetime.datetime(2016,6,26,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,26,21,0), 1.5],
        [datetime.datetime(2016,6,26,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,27,0,0), 0.9],
        
        [datetime.datetime(2016,6,27,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,27,4,0), 0.8],
        [datetime.datetime(2016,6,27,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,27,21,0), 1.5],
        [datetime.datetime(2016,6,27,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,28,0,0), 0.9],]
    
    basalRecord3=[
        [datetime.datetime(2016,6,21,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,21,4,0), 0.4],
        [datetime.datetime(2016,6,21,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,21,21,0), 0.8],
        [datetime.datetime(2016,6,21,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,22,0,0), 0.4],
        
        [datetime.datetime(2016,6,22,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,22,4,0), 0.4],
        [datetime.datetime(2016,6,22,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,22,21,0), 0.8],
        [datetime.datetime(2016,6,22,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,23,0,0), 0.4],
        
        [datetime.datetime(2016,6,23,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,23,4,0), 0.4],
        [datetime.datetime(2016,6,23,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,23,21,0), 0.8],
        [datetime.datetime(2016,6,23,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,24,0,0), 0.4],
        
        [datetime.datetime(2016,6,24,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,24,4,0), 0.4],
        [datetime.datetime(2016,6,24,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,24,21,0), 0.8],
        [datetime.datetime(2016,6,24,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,25,0,0), 0.4],
        
        [datetime.datetime(2016,6,25,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,25,4,0), 0.4],
        [datetime.datetime(2016,6,25,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,25,21,0), 0.8],
        [datetime.datetime(2016,6,25,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,26,0,0), 0.4],
        
        [datetime.datetime(2016,6,26,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,26,4,0), 0.4],
        [datetime.datetime(2016,6,26,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,26,21,0), 0.7],
        [datetime.datetime(2016,6,26,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,27,0,0), 0.4],
        
        [datetime.datetime(2016,6,27,0,0), 'BAS', 4*3600, datetime.datetime(2016,6,27,4,0), 0.4],
        [datetime.datetime(2016,6,27,4,0), 'BAS', 17*3600, datetime.datetime(2016,6,27,21,0), 0.7],
        [datetime.datetime(2016,6,27,21,0), 'BAS', 3*3600, datetime.datetime(2016,6,28,0,0), 0.4],]
        
    #return basalRecord
    if no==0:return basalRecord1
    elif no==1:return basalRecord2
    elif no==2:return basalRecord3

def getBolusRecord(no):
    bolusRecord=[]
    t=datetime.datetime(2016, 6, 19, 9, 20, 0)
    bolusRecord.append([t, 'NBM', 1.0, 1.0])
    t=datetime.datetime(2016, 6, 19, 14, 10, 0)
    bolusRecord.append([t, 'NBM', 2.5, 2.5])
    #
    t=datetime.datetime(2016, 6, 20, 10, 30, 0)
    bolusRecord.append([t, 'NBM', 3.2, 3.2])
    t=datetime.datetime(2016, 6, 20, 16, 20, 0)
    bolusRecord.append([t, 'NBM', 4.0, 4.0])
    #
    t=datetime.datetime(2016, 6, 21, 8, 50, 0)
    bolusRecord.append([t, 'NBM', 5.0, 5.0])
    t=datetime.datetime(2016, 6, 21, 17, 10, 0)
    bolusRecord.append([t, 'NBM', 2.0, 2.0])
    #
    t=datetime.datetime(2016, 6, 22, 10, 20, 0)
    bolusRecord.append([t, 'NBM', 6.0, 6.0])
    t=datetime.datetime(2016, 6, 22, 19, 50, 0)
    bolusRecord.append([t, 'NBM', 1.5, 1.5])
    
    bolusRecord1=[
        [datetime.datetime(2016,6,21,11,30), 'NBM', 6, 6],
        [datetime.datetime(2016,6,21,17,30), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,22,7,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,22,11,30), 'NBM', 6, 6],
        [datetime.datetime(2016,6,22,17,30), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,23,7,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,23,11,30), 'NBM', 7, 7],
        [datetime.datetime(2016,6,23,17,30), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,24,7,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,24,11,30), 'NBM', 7, 7],
        [datetime.datetime(2016,6,24,17,30), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,25,7,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,25,11,30), 'NBM', 8, 8],
        [datetime.datetime(2016,6,25,18,00), 'NBM', 6, 6],
        
        [datetime.datetime(2016,6,26,8,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,26,12,0), 'NBM', 6, 6],
        [datetime.datetime(2016,6,26,18,0), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,27,8,0), 'NBM', 7, 7],
        [datetime.datetime(2016,6,27,12,0), 'NBM', 6, 6],
        [datetime.datetime(2016,6,27,18,0), 'NBM', 7, 7],]
    
    bolusRecord2=[
        [datetime.datetime(2016,6,21,7,30), 'NBM', 8, 8],
        [datetime.datetime(2016,6,21,12,0), 'NBM', 9, 9],
        [datetime.datetime(2016,6,21,18,30), 'NBM', 8, 8],
        
        [datetime.datetime(2016,6,22,7,30), 'NBM', 10, 10],
        [datetime.datetime(2016,6,22,12,0), 'NBM', 9, 9],
        [datetime.datetime(2016,6,22,18,30), 'NBM', 9, 9],
        
        [datetime.datetime(2016,6,23,7,30), 'NBM', 12, 12],
        [datetime.datetime(2016,6,23,12,0), 'NBM', 10, 10],
        [datetime.datetime(2016,6,23,18,30), 'NBM', 11, 11],
        
        [datetime.datetime(2016,6,24,7,30), 'NBM', 12, 12],
        [datetime.datetime(2016,6,24,12,0), 'NBM', 10, 10],
        [datetime.datetime(2016,6,24,18,30), 'NBM', 11, 11],
        
        [datetime.datetime(2016,6,25,7,30), 'NBM', 12, 12],
        [datetime.datetime(2016,6,25,12,0), 'NBM', 10, 10],
        [datetime.datetime(2016,6,25,18,30), 'NBM', 11, 11],
        
        [datetime.datetime(2016,6,26,7,30), 'NBM', 11, 11],
        [datetime.datetime(2016,6,26,12,0), 'NBM', 10, 10],
        [datetime.datetime(2016,6,26,18,30), 'NBM', 12, 12],
        
        [datetime.datetime(2016,6,27,7,30), 'NBM', 11, 11],
        [datetime.datetime(2016,6,27,12,0), 'NBM', 10, 10],
        [datetime.datetime(2016,6,27,18,30), 'NBM', 11, 11],
        ]
    
    bolusRecord3=[
        [datetime.datetime(2016,6,21,8,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,21,12,30), 'NBM', 6, 6],
        [datetime.datetime(2016,6,21,18,30), 'NBM', 6, 6],
        
        [datetime.datetime(2016,6,22,8,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,22,12,30), 'NBM', 5, 5],
        [datetime.datetime(2016,6,22,18,30), 'NBM', 6, 6],
        
        [datetime.datetime(2016,6,23,8,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,23,12,30), 'NBM', 4, 4],
        [datetime.datetime(2016,6,23,18,30), 'NBM', 5, 5],
        
        [datetime.datetime(2016,6,24,8,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,24,12,30), 'NBM', 5, 5],
        [datetime.datetime(2016,6,24,18,30), 'NBM', 5, 5],
        
        [datetime.datetime(2016,6,25,8,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,25,12,30), 'NBM', 5, 5],
        [datetime.datetime(2016,6,25,18,30), 'NBM', 5, 5],
        
        [datetime.datetime(2016,6,26,9,0), 'NBM', 5, 4],          
        [datetime.datetime(2016,6,26,12,30), 'NBM', 4, 4],
        [datetime.datetime(2016,6,26,19,0), 'NBM', 6, 6],
        
        [datetime.datetime(2016,6,27,9,0), 'NBM', 6, 6],          
        [datetime.datetime(2016,6,27,12,30), 'NBM', 5, 5],
        [datetime.datetime(2016,6,27,19,0), 'NBM', 6, 6],]

    if no==0:return bolusRecord1
    elif no==1:return bolusRecord2
    elif no==2:return bolusRecord3
    
    # 
    #return bolusRecord
    
def func1():
    for i in range(0,3):
        basalRecord=getBasalRecord(i)
        for record in basalRecord:
            debug.printraw(record)
            
        # 分割线 
        #
        bolusRecord=getBolusRecord(i)
        for record in bolusRecord:
            debug.printraw(record)
        
        # 保存到文件
        strRes1=dumpBasalRecord(basalRecord)
        debug.trace(strRes1)
        strRes2=dumpBolusRecord(bolusRecord)
        debug.trace(strRes2)
        # 
        with open('basal_%d.txt'%(i+1), 'w') as f:
            f.write(strRes1)
            
        with open('bolus_%d.txt'%(i+1), 'w') as f:
            f.write(strRes2)    
    
    
    
if __name__=='__main__':
    func1()