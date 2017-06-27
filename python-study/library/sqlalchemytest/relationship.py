#!usr/bin/env python
#coding:utf-8

import datetime
import time

import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, aliased, relationship, backref
from sqlalchemy import func, and_, or_


class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def printraw(self, obj):
        print obj

debug = Debug()

Base = declarative_base()
'''
class Student(Base):
    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    banji_id=

class Banji(Base):
    id=Column(Integer, primary_key=True)
    
class Course(Base):
    id=Column(Integer, primary_key=True)    
    name='''

# relationship必须是基于外键的 
class Parent(Base):
    __tablename__='parent'
    id=Column(Integer, primary_key=True)
    children=relationship("Child", backref='parent')
    
class Child(Base):
    __tablename__='child'
    id=Column(Integer, primary_key=True)
    parent_id=Column(Integer, ForeignKey('parent.id'))
    #parent_id=Column(Integer)

    
class RelationDemo(object):

    def __init__(self):
        engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
        #print dir(engine)
        # 这种用法在SQLAlchemy里面称为声明系统。使用声明系统来实现跟数据库表的映射不是
        # 必须的，可以直接使用Table对象来实现映射。
        Session = sessionmaker(bind=engine)
        self.session = Session()
        Base.metadata.create_all(engine)
    
    def load_data(self):
        try:
            parent=Parent(id=1)
            child1=Child(id=1,parent_id=1)
            child2=Child(id=2,parent_id=1)
            child3=Child(id=3,parent_id=1)
            self.session.add(parent)
            self.session.add_all([child1, child2, child3])
            self.session.commit()
        except Exception,e:
            self.session.rollback()
            debug.trace('load data fail')    
        
    def query_by_relationship(self):
        parent=self.session.query(Parent).filter(Parent.id==1).first()
        children=parent.children
        debug.trace(['parent.children:', type(parent.children)])
        for c in children:debug.trace(['c.id:', c.id, c.parent.id])
        
    def start(self):
        self.load_data()
        self.query_by_relationship()
        
if __name__=='__main__':
    demo=RelationDemo()
    demo.start()
    