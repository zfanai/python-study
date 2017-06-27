#encoding:gbk
'''
1.如果列的类型改变时，原先的值可以转换为新的类型值时
  则进行自动的类型转换。如果不能进行类型转换为新类型
  的值。则会报错，不能进行表的类型修改。所以如果要进
  行表的列类型转换时，如果报错就需要手动操作进行类型
  转换
2.数据库的类型设计如果专而细，就可以利用数据库的一些
  类型检查等等功能，如果设计抽象而通用，类如都用字符
  串表示，修改方便，但是就不能利用数据库的类型检查等
  功能。所以不可两者兼得。这有点类似于强类型语言和弱
  类型语言的不同哲学。
'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func
from datetime import *

class Debug(object):
    def trace(self, obj):
        print "trace:", obj

debug = Debug()

#

session=None
def init():
    global session
    #
    #engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
    #engine = create_engine('mysql://root:myzfsql85@localhost/testdb', echo=False)
    engine = create_engine('mysql://zhoufan:myzfsql85@192.168.40.202/testdb', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session() 

def create_table():
    strsql= 'CREATE TABLE if not exists `tbl1` ('+\
            '    `id` int NOT NULL AUTO_INCREMENT,'+\
            '    `day` date DEFAULT NULL,'+\
            '    PRIMARY KEY (`id`)'+\
            ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    session.execute(strsql)
    
    strsql= 'CREATE TABLE if not exists `tbl2` ('+\
            '    `id` int NOT NULL AUTO_INCREMENT,'+\
            '    `day` varchar(16) DEFAULT NULL,'+\
            '    PRIMARY KEY (`id`)'+\
            ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    session.execute(strsql)
    session.commit()

def gen_data():
    data=[]
    data.append({'day':'2015-07-10'})
    data.append({'day':'2015-07-09'})
    return data
def load_data(data):
    strsql='INSERT INTO `tbl2` (day) VALUES '+\
           '("2015-07-10a"),'+\
           '("2015-07-09a");'
    session.execute(strsql)
    session.commit()

def change_column():
    #strsql='alter table tbl2 modify day varchar(16);'
    strsql='alter table tbl2 modify day date;'
    session.execute(strsql)
    session.commit()
    
if __name__=='__main__':
    init()
    create_table()
    load_data(gen_data())
    change_column()
    #read_data()