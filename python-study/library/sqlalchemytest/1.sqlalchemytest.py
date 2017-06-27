#!usr/bin/env python
#coding:utf-8

import datetime
import time

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func, and_, or_


SG_INTERVAL=2

class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def printraw(self, obj):
        pass
        print obj

debug = Debug()
#
print sqlalchemy.__version__
engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
#print dir(engine)

# 这种用法在SQLAlchemy里面称为声明系统。使用声明系统来实现跟数据库表的映射不是
# 必须的，可以直接使用Table对象来实现映射。
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# String如果没有指定大小的话，在MySQL作为驱动数据库时会报错，必须指定
# 字符串的大小。
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(16))
    fullname = Column(String(16))
    password = Column(String(16))
    
    def __repr__(self):
        return "<User (name='%s', fullname='%s',password='%s')>" % (
                        self.name, self.fullname, self.password)

#class Records
class SensorGlucoseRecord(Base):
    __tablename__ = 'sensor_glucose_record'
    id = Column(String(64), primary_key = True)
    user_id = Column(Integer)
    sensor_id = Column(String(64))
    session_id = Column(String(64))
    #date
    #time
    time = Column(DateTime)
    sensor_state = Column(String(4))
    glucose_value = Column(Float)
    signal_value = Column(Float)
    rate = Column(Float)
    #
    def __repr__(self):
        return '<SensorGlucoseRecord %r>' % (self.glucose_value)

#class Records
class SG(Base):
    __tablename__ = 'sg'
    id = Column(String(64), primary_key = True)
    user_id = Column(Integer)
    sensor_id = Column(String(64))
    session_id = Column(String(64))
    #date
    #time
    time = Column(DateTime)
    sensor_state = Column(String(4))
    glucose_value = Column(Float)
    signal_value = Column(Float)
    rate = Column(Float)
    #
    def __repr__(self):
        return '<SensorGlucoseRecord %r>' % (self.glucose_value)

        #class Records
class SG1(Base):
    __tablename__ = 'sg1'
    id = Column(String(64), primary_key = True)
    user_id = Column(Integer)
    sensor_id = Column(String(64))
    session_id = Column(String(64))
    #date
    #time
    day = Column(String(8))  #日期
    time = Column(DateTime)
    sensor_state = Column(String(4))
    glucose_value = Column(Float)
    signal_value = Column(Float)
    rate = Column(Float)
    #
    def __repr__(self):
        return '<SensorGlucoseRecord %r>' % (self.glucose_value)
        
# 怎么把类名都做参数。        
def load_data(uid, sd, dn):
    pass
    for id in uid:
        for d in range(0,dn):
            debug.trace(["load_data:uid,d:", uid, d])
            td=sd+datetime.timedelta(days=d)
            for n in range(0,720):
                
                tdm=td+datetime.timedelta(minutes=n*SG_INTERVAL)
                sg=SensorGlucoseRecord(
                    id="%05d%s%03d" % (id, td.strftime("%Y%m%d"), n),
                    user_id=id,
                    time=tdm,
                    sensor_state="C",
                    glucose_value="6.5",
                    signal_value="20.3",
                    rate="0.02"
                )
                session.add(sg)
                if (n+1)%100==0:
                    session.commit()
            session.commit()
            
# 怎么把类名都做参数。        
def load_data2(uid, sd, dn):
    pass
    for id in uid:
        for d in range(0,dn):
            debug.trace(["load_data:uid,d:", id, d])
            td=sd+datetime.timedelta(days=d)
            for n in range(0,720):
                
                tdm=td+datetime.timedelta(minutes=n*SG_INTERVAL)
                sg=SG(
                    id="%05d%s%03d" % (id, td.strftime("%Y%m%d"), n),
                    user_id=id,
                    time=tdm,
                    sensor_state="C",
                    glucose_value="6.5",
                    signal_value="20.3",
                    rate="0.02"
                )
                session.add(sg)
                if (n+1)%100==0:
                    session.commit()
            session.commit()

# 怎么把类名都做参数。        
def load_data3(uid, sd, dn):
    pass
    for id in uid:
        for d in range(0,dn):
            debug.trace(["load_data:uid,d:", id, d])
            td=sd+datetime.timedelta(days=d)
            for n in range(0,720):
                
                tdm=td+datetime.timedelta(minutes=n*SG_INTERVAL)
                sg=SG1(
                    id="%05d%s%03d" % (id, td.strftime("%Y%m%d"), n),
                    user_id=id,
                    day=td.strftime("%Y%m%d"),
                    time=tdm,
                    sensor_state="C",
                    glucose_value="6.5",
                    signal_value="20.3",
                    rate="0.02"
                )
                session.add(sg)
                if (n+1)%100==0:
                    session.commit()
            session.commit()
            
def func1():
    pass
    Base.metadata.create_all(engine)
    #sd=datetime.datetime(2015,1,1)
    #load_data(range(1,10), sd, 10)

def func2():
    pass
    #rv=session.query(func.count(SensorGlucoseRecord)).all()
    #debug.trace(["func2:rv size:", rv])
    
    #rv=session.query(SensorGlucoseRecord).all()
    #debug.trace(["func2:rv size:", len(rv)])
    
    # 用这种方法查询个数很快
    rv=session.query(SensorGlucoseRecord).count()
    debug.trace(["func2:rv size:", rv])
    
    user_id=1
    #STABLE_CALIB
    dt_low=datetime.datetime(2015,1,1,0,0)
    dt_high=datetime.datetime(2015,1,1,1,0)
    est=time.time()
    rv = session.query(
                SensorGlucoseRecord.time, 
                SensorGlucoseRecord.glucose_value,SensorGlucoseRecord.rate).filter(
                and_(SensorGlucoseRecord.time >= dt_low, SensorGlucoseRecord.time < dt_high)).filter(
                SensorGlucoseRecord.user_id == user_id).filter(
                or_(SensorGlucoseRecord.sensor_state == "C",SensorGlucoseRecord.sensor_state == "NC")).order_by(SensorGlucoseRecord.time).all()    
    eet=time.time()
    debug.trace(["func2:exe time:", (eet-est)])
    debug.trace(["func2:rv size:", len(rv)])

def func3():
    sd=datetime.datetime(2014,1,1)
    load_data2(range(2, 20), sd, 365)

def func4():
    est=time.time()
    rv=session.query(SG).count()
    eet=time.time()
    # 查询个数的时间，499万条记录，查询时间14秒
    debug.trace(["func2:exe time:", (eet-est)])
    
    debug.trace(["func2:rv size:", rv])

def func5():
    # 只限定了一个变量的查询时间是0.134秒
    dt=datetime.datetime(2014,7,8,13,6)
    est=time.time()
    rv=session.query(SG).filter(SG.time==dt).first()
    eet=time.time()
    debug.trace(["func5:exe time:t1:", (eet-est)])
    debug.trace(["rv:", rv.id, rv.glucose_value])
    # 有两个限定条件的查询耗时2.4秒。
    dt=datetime.datetime(2014,7,8,13,6)
    est=time.time()
    #rv=session.query(SG).filter(SG.time==dt).filter(SG.user_id==10).first()
    rv=session.query(SG).filter(and_(SG.time==dt, SG.user_id==10)).first()
    eet=time.time()
    debug.trace(["func5:exe time:t2:", (eet-est)])
    debug.trace(["rv:", rv.id, rv.glucose_value])
    
    # 通过时间范围的方式来查找，耗时4.9秒,跟时间范围的大小关系不大。
    dt1=datetime.datetime(2014,7,8,13,6)
    dt2=datetime.datetime(2014,7,9,13,7)
    est=time.time()
    rv=session.query(SG).filter(and_(SG.time>=dt1, SG.time<dt2, SG.user_id==10)).all()
    eet=time.time()
    # 通过时间范围的方式来查找，耗时4.9秒
    debug.trace(["func5:exe time:t3:", (eet-est)])
    debug.trace(["rv:size:", len(rv)])

# 加载数据
def load_data_sg1():
    sd=datetime.datetime(2014,1,1)
    load_data3(range(2, 20), sd, 365)    

# @note 使用day字段的时候查询时间的对比
# 查询时间差不多
def sg1_query_test():
    #est=time.time()
    #rv=session.query(SG1).count()
    #eet=time.time()
    dt=datetime.datetime(2014,7,8,13,6)
    est=time.time()
    rv=session.query(SG1).filter(SG1.time==dt).first()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t1:", (eet-est)])
    debug.trace(["rv:", rv.id, rv.glucose_value, rv.day])   
    
    # 根据日期查询
    
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.day>="20140706", SG1.day<="20140716", SG1.user_id==10)).all()
    eet=time.time()
    # 查询需要11秒
    debug.trace(["sg1_query_test:exe time:t2:", (eet-est)])
    #
    dt1=datetime.datetime(2014,7,6)
    dt2=datetime.datetime(2014,7,16)
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.time>=dt1, SG1.day<=dt2, SG1.user_id==10)).all()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t3:", (eet-est)])
    
    # 查询某一天的数据, 采用天作为索引的方式查询的时间差不多。
    # 和采用时间范围的方式的时间差不多。但是读取一天的数据和读取10天的数据的查询时间差不多。
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.day=="20140706", SG1.user_id==10)).all()
    eet=time.time()
    # 查询需要11秒
    debug.trace(["sg1_query_test:exe time:t4:", (eet-est), len(rv)])
    dt1=datetime.datetime(2014,7,6)
    dt2=datetime.datetime(2014,7,7)
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.time>=dt1, SG1.time<=dt2, SG1.user_id==10)).all()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t5:", (eet-est), len(rv)])

# @note 查询一天的数据和多天的数据时间的对比。
# 查询一天的数据的时间是4.8秒，查询10天的数据的时间是5.1秒，差别不大。   
# 499万条记录的情况。 这个是20个用户，每个用户一年的数据。
def sg1_query1(): 
    # 
    rv=session.query(SG1).count()
    debug.trace(["sg1 count:", rv])
    # 
    dt1=datetime.datetime(2014,7,6)
    dt2=datetime.datetime(2014,7,7)
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.time>=dt1, SG1.time<=dt2, SG1.user_id==10)).all()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t5:", (eet-est), len(rv)])
    #
    dt1=datetime.datetime(2014,7,6)
    dt2=datetime.datetime(2014,7,16)
    est=time.time()
    rv=session.query(SG1).filter(and_(SG1.time>=dt1, SG1.time<=dt2, SG1.user_id==10)).all()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t6:", (eet-est), len(rv)])

# @note filter函数使用sql语句作为参数
def sg1_query2():
    #
    est=time.time()
    rv=session.query(SG1).filter("sg1.user_id=10 and sg1.time>'2014-07-06 02:00' and sg1.time<'2014-07-07 02:20'").all()
    eet=time.time()
    debug.trace(["sg1_query_test:exe time:t6:", (eet-est), len(rv)])
#
if __name__ == "__main__":
    func1()
    #func2()
    #func3()
    #func4()
    #func5()
    #load_data_sg1()
    #sg1_query_test()
    sg1_query2()

    
    