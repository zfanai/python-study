#!usr/bin/env python
# -*- coding: utf-8 -*
import datetime
import time

class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def rprint(self, obj):
        print obj
debug = Debug()

# 日期的格式化
# 日期的比较
def func1():
    # 获得当前的时间
    dt = datetime.datetime.now()
    debug.trace(['dt:', dt]) 
    #
    print "sadfef"
    dt = datetime.datetime(2014,4,9)
    timespan = datetime.timedelta(minutes=2)
    dt2 = dt + timespan
    print dt.strftime("%Y-%m-%d%H%M%S")
    print dt.strftime("%Y-%m-%d")
    print dt2.strftime("%Y%m%d%H%M%S")
    
    dt3 = datetime.datetime(2014,4,9,5,6,7)
    dt4 = datetime.datetime(2014,4,9,5,6,8)
    dt5 = datetime.datetime(2014,4,9,5,6,9)
    print dt4 > dt3
    print dt4 > dt5

# time是一个模块
# datetime.time是一个类型，timestamp的输入不能早于1970-01-01
def func2():
    start_date= datetime.datetime(1970,1,2)
    start_time = start_date.time()
    debug.trace(['type(start_time)', type(start_time)]) 
    debug.trace(['type(datetime.time)', type(datetime.time)]) 
    
    # time.time()获得当前的UNIX纪元时间, 在Python系统里面有两个
    # time属性，一个是datetime模块里面有一个time属性，还有一个是
    # time模块，time模块里面也有time属性。
    timeobj=time.time()
    debug.trace(['type(time)', type(time) ])
    debug.trace(['type(timeobj)', type(timeobj), timeobj])
    
    #
    timetuple = start_date.timetuple()
    debug.trace([ "timetuple:",type(timetuple),timetuple])
    
    
    # 沟通了datetime和timestamp
    timestamp = time.mktime(timetuple)
    debug.trace(["timestamp:", timestamp, type(timestamp)])
    
    # localtime和mktime是一对反函数。
    ltime = time.localtime(timestamp)
    debug.trace(["ltime:", ltime, type(ltime)]) 
    
    timeStr = time.strftime("%Y-%m-%d", ltime)
    debug.trace(["timeStr:", timeStr])
    # 
    d1=datetime.datetime.fromtimestamp(timestamp)
    debug.trace(["d1:", d1.strftime("%Y-%m-%d")])
    
# timedelta沟通秒和日期之间的转换
def func3():
    start_date= datetime.datetime(1960,1,2)
    end_date= datetime.datetime(1960,1,3)
    print start_date
    delta = end_date-start_date
    #print 
    seconds=delta.total_seconds()
    print seconds
    
    print type(delta)
    
    temp_date = start_date+datetime.timedelta(seconds=seconds*2)
    print temp_date

# 时区因素
def func31():
    print "test_timezone"
    #print time.timezone  
    ofs=time.timezone    # 当前时区跟UTC的偏移
    print ofs

# @note 日期类
def func4():
    n=datetime.datetime.now()
    d1=n.date()
    d2=datetime.date(2015,6,22)
    t=d1-d2
    debug.trace(["t:", t.days])
    d3=datetime.date(1600,6,1)
    debug.rprint(["d3:", d3])
    strd3=d3.strftime('%Y-%m-%d')  #格式化函数要求年数在1900年以后。

# 时间类
def func5():
    n=datetime.datetime.now()
    t=n.time()
    debug.trace(["t:", t])
    t=datetime.time(8,2)
    debug.trace(["n:", n])

# 
def func6():
    # 1441428630, 1441515030都是本地时间。
    #tl=[1441428630, 1441515030, 1441399939]
    #tl = [1441544345.62, 1441457945.62, 1441400419]
    #tl=[1441573403.153, 1441487003.153, 1441400659]
    #tl=[1441487179.0, 1441400779.0, 1441400779, 1442511006, 1445626541, 1448518390, 1448518474]
    # 3600秒打印出来的时间是9点。
    #tl=[1448518390, 1448518474, 1448519120, 3600, 1448490197]
    #tl=[1449417690, 1449417810, 1449676828]
    tl=[1455552000,1455602890,1455602922,1455602979,1455607255,1455607293]
    for t in tl:
        d1=datetime.datetime.fromtimestamp(t)
        #d1=datetime.datetime.utcfromtimestamp(t)
        debug.trace(["d1:", d1.strftime("%Y-%m-%d %H:%M:%S")])
    #
    t=1448519120
    d1=datetime.datetime.fromtimestamp(t)
    debug.trace(["d1:", d1, t])
    #
    sec=time.mktime(d1.timetuple())  #+time.timezone
    debug.trace(["sec:", sec])    #1448490320
    
if __name__ == '__main__':
    #func1()
    #func2()
    #func3()
    #func31()
    #func4()
    #func5()
    func6()
    
    