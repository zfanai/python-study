#encoding:gbk

import sys
import datetime
import random

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func


class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
    def rprint(self, msg):
        print msg
debug=Debug()

Session=None
uid=83
sn=102000120
idPrefix='%d-%d-'%(uid, sn)
     
def initdb(pwd, db):
    global Session
    #
    #engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
    engine = create_engine('mysql://root:%s@localhost/%s' % (pwd, db), echo=False)
    Session = sessionmaker(bind=engine)
    #session = Session()    

def randomStr(size=10):
    charlist=[]
    charlist += range(ord('0'), ord('9'))
    charlist += range(ord('a'), ord('z'))
    num=len(charlist)
    rvstr=""
    i=0
    while i<size:
        i += 1
        index=int(num*random.random())
        rvstr+=chr(charlist[index])
    return rvstr
 
def deleteSG(uid, st):
    session=Session()
    strsql='delete from sensor_glucose_record where user_id=%d and time>=\'%s\'' % (uid, st)
    session.execute(strsql)
    session.commit()
    
def insertSG(data):
    session=Session()
    strsql='''
    insert into sensor_glucose_record  (id, user_id, sensor_id, time, sensor_state, glucose_value, 
    signal_value, rate) values '''
    count=0
    size=len(data)
    rowstr=""
    startTime=datetime.datetime.strptime(data[0][0], '%Y-%m-%d %H:%M:%S')
    endTime=datetime.datetime.strptime(data[-1][0], '%Y-%m-%d %H:%M:%S')
    ndt=datetime.datetime.now()
    deltaTime=ndt-startTime
    timeRange=endTime-startTime
    debug.trace(["deltaTime:", deltaTime])
    debug.trace(["timeRange:", timeRange])
    timeOffset=ndt-endTime
    debug.trace(["timeOffset:", timeOffset])
    
    #
    for item in data:
        #id=randomStr(16)
        rowId='%s-%04d'%(idPrefix, count+1)
        dt=item[0]
        sg=item[1]
        #
        sgTime=datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        sgTime+=datetime.timedelta(days=timeOffset.days+1)
        #
        if sgTime>ndt:
            if count>0:
                rowstr+=';'
            break
        else:
            if count==0:
                pass
            elif count==size-1:
                rowstr += ';'
            else:
                rowstr += ','
        
        #
        dt=sgTime.strftime('%Y-%m-%d %H:%M:%S')
        #
        sgr=sg/80
        sig=sg*3
        lineStr='(\'%s\', %d, %d, \'%s\', \'C\', %.2f, %.2f, %.4f)' % (rowId, uid, sn,dt, sg, sig, sgr)
        rowstr += lineStr
        
        #if count==size-1:
        #    rowstr += ';'
        #else:
        #    rowstr += ','
        #debug.trace(['lineStr:', lineStr])
        #
        count+=1
    #
    strsql += rowstr
    #debug.trace(['strsql:', strsql])
    session.execute(strsql)
    session.commit()
    #
    
def insertDeviceActivateRecord(uid, deviceType, deviceSN, st):
    session=Session()
    strsql='''
    insert into device_activate_record  (uid, devicetype, devicesn, startTime, endTime, action) values(
    %d, '%s', %d, '%s', '%s', '%s') 
    ''' % (uid, deviceType, deviceSN, st, st, 'activate')
    session.execute(strsql)
    session.commit()
    
def readData(fn):
    fo=open(fn, 'r')
    lines=fo.readlines()
    data=[]
    count=0
    for line in lines:
        dt,sg=line.strip().split(',')
        #debug.trace(['dt,sg:', dt, sg])
        count += 1
        #if count>=10:
        #    break
        if count%100==0:
            debug.trace(['count:', count])
        #
        #dt=datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        sg=float(sg)
        data.append([dt, sg])
    debug.trace(['count:', count])
    return data
#
if __name__=='__main__':
    #xlsfile=sys.argv[1]
    #nMaxRow=sys.argv[2]
    pwd=sys.argv[1]
    db=sys.argv[2]
    fn=sys.argv[3]
    #
    #func1(xlsfile, nMaxRow)
    data=readData(fn)
    startTime=data[0][0]
    initdb(pwd, db)
    deleteSG(83, startTime)
    insertSG(data)
    #insertDeviceActivateRecord(83, 'ty', 102000120, startTime)
    