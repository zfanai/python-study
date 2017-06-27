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
        print obj
#
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


        
# 怎么把类名都做参数。        
def loadData(uid, sd, dn):
    pass
                    
def func1():
    pass
    Base.metadata.create_all(engine)

# @note 测试删除。
def func2():
    count=session.query(User).count()
    debug.trace(["count:", count])
    #for record in session.query(User).all():
    #    debug.trace(["user.id", record.id])
    for record in session.query(User).filter("id in (10,11)").all():
        debug.trace(["user.id", record.id])
    session.query(User).filter(and_(User.id>=10, User.id<=14)).delete()
    session.commit()  # 不commit是不会删除的。
    for record in session.query(User).filter("id in (10,11)").all():
        debug.trace(["user.id", record.id])
#
if __name__ == "__main__":
    func1()
    func2()


    
    