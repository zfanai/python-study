#!usr/bin/env python
#coding:gbk

import datetime
import time
import re

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func, and_, or_


class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def printraw(self, obj, save=False):
        print obj
        if save:
            n=datetime.datetime.now()
            fn='log_%s.txt' % n.strftime('%Y%m%d')
            fo=open(fn,'a')
            fo.write(str(obj)+'\n')
            fo.close()
#
debug = Debug()

#
session=None
def initdb():
    global session
    #
    engine = create_engine('mysql://root:myzfsql85@localhost/ultrax2', echo=False)
    #print dir(engine)

    # 这种用法在SQLAlchemy里面称为声明系统。使用声明系统来实现跟数据库表的映射不是
    # 必须的，可以直接使用Table对象来实现映射。
    #Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

def func1():
    strsql='show tables;'
    rv=session.execute(strsql)
    debug.trace(['rv:', rv])
    #
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row, save=True)

def table_desc(tbl):
    strsql='desc %s;' % tbl
    rv=session.execute(strsql)
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row)
def func2():
    strsql='desc pre_ucenter_pm_lists;'
    rv=session.execute(strsql)
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row)
        
    strsql='select * from pre_ucenter_pm_lists;'
    rv=session.execute(strsql)
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row)

def func3():
    
    for i in range(0,10):
        tbl='pre_ucenter_pm_messages_%d;' % i
        table_desc(tbl)
        strsql='select * from %s' % tbl
        debug.trace(['strsql:', strsql])
        rv=session.execute(strsql)
        num=rv.rowcount
        for i in range(0,num):
            row=rv.fetchone()
            debug.printraw(row)

def table_lsdata(tbl):
    strsql='select * from %s;' % tbl
    #debug.trace(['strsql:', strsql])
    rv=session.execute(strsql)
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row)    
#
def func4():
    table_desc('pre_home_friend')
    strsql='select * from pre_home_friend'
    #debug.trace(['strsql:', strsql])
    rv=session.execute(strsql)
    num=rv.rowcount
    for i in range(0,num):
        row=rv.fetchone()
        debug.printraw(row)
def func5():
    debug.trace('pre_ucenter_pm_members')
    table_desc('pre_ucenter_pm_members')
    table_lsdata('pre_ucenter_pm_members')
    debug.trace('pre_ucenter_pm_lists')
    
    table_desc('pre_ucenter_pm_lists')
    table_lsdata('pre_ucenter_pm_lists')

def func6(f):
    fo=open(f, 'r')
    line=fo.readline()
    while len(line)>0:
        #debug.printraw(line)
        #
        m=re.search('CREATE TABLE (\w+) \(', line)
        #debug.trace(['m:', m])
        if m is not None:
            #debug.trace(['group:', m.group(1)])
            debug.printraw('(%s,)' % m.group(1), save=True)
        #
        line=fo.readline()
def func7():
    func6('install.sql')
    #func6('uc.sql')

def func8():
    tbllist=['pre_common_friendlink', 'pre_home_friend', 'pre_home_friend_request', 
            'pre_home_friendlog', 'pre_ucenter_friends', 'pre_ucenter_members']
    #
    for tbl in tbllist:
        debug.trace(['tbl:', tbl, '=============================='])
        table_desc(tbl)
        table_lsdata(tbl)
        print '\n'
        
    
#
if __name__ == "__main__":
    initdb()
    #func1()
    #func2()
    #func3()
    #func5()
    #func7()
    func8()
    


    
    