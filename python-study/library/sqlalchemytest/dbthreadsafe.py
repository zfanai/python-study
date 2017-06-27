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
2016-7-30 同一个session如果多线程如果没有设置好锁，访问
会出错。所以一般是每个线程都创建自己的session。  
'''
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func
from datetime import *

class Debug(object):
    def trace(self, obj):
        print "trace:", obj

debug = Debug()

#
Session=None
session=None
session2=None
def init():
    global Session
    global session
    global session2
    #
    #engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
    # 跟设置项有关，比如事务处理啊，自动提交啊，这项设置项。
    # 如果每次操作数据库都是重新打开连接，执行完再关闭连接的话就不会有这些问题，但是
    # 这种做法效率比较低，因为数据的打开连接，关闭连接都比较耗费时间。
    engine = create_engine('mysql://root:myzfsql85@localhost/testdb', echo=False, pool_size=10, pool_recycle=7200)
    #engine = create_engine('mysql://root:myzfsql85@localhost/testdb', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    debug.trace(['type of session:', type(session)])
    #session2 = Session()    

def create_table():
    strsql= '''
    CREATE TABLE if not exists tbl1 (
        id int NOT NULL AUTO_INCREMENT,
        day date DEFAULT NULL,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    session.execute(strsql)
    
    '''
    strsql= 'CREATE TABLE if not exists `tbl2` ('+\
            '    `id` int NOT NULL AUTO_INCREMENT,'+\
            '    `day` varchar(16) DEFAULT NULL,'+\
            '    PRIMARY KEY (`id`)'+\
            ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    session.execute(strsql)
    '''
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

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        apply(self.func, self.args)

Base = declarative_base()

# String如果没有指定大小的话，在MySQL作为驱动数据库时会报错，必须指定
# 字符串的大小。
class Tbl2(Base):
    __tablename__ = 'tbl2'
    id = Column(Integer, primary_key = True)
    day = Column(String(16))
    
# 如果不同的线程使用不同的session是可以成功的。
# 但是如果同一个 session ，多线程访问是会失败的。        
def load_data_t(index):
    strsql=None
    if True:
        strsql='INSERT INTO `tbl2` (day) VALUES '+\
               '("2015-07-10"),'+\
               '("2015-07-09");'
    else:
        strsql='select * from tbl2;'
    #session=Session()
    if index==0:
        session.execute(strsql)
        debug.trace(['index:', index])
        # session不commit是不会写进数据库的。
        session.commit()
    elif index==1:
        session.execute(strsql)
        debug.trace(['index:', index])
        #session.commit()

def load_data_t2(index):
    rv=session.query(Tbl2).all()
    #session.commit()
    for item in rv:
        debug.trace(['id:', item.id])

# 这里依然会报错，但是在flask框架里面用db.session来测试的时候没有报错。        
def load_data_t3(index):
    obj1=Tbl2(day='2015-07-21')
    session.add(obj1)
    session.commit()
    
# 多线程访问会失败。
def thread_loaddata():
    threads = []
    nloops = range(1)

    for i in nloops:
        t = MyThread(load_data_t, (i, ))
        #t = MyThread(load_data_t2, (i, ))
        #t = MyThread(load_data_t3, (i, ))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

def func1():
    while raw_input('press q to quit.\n')=='q':
        break
        
if __name__=='__main__':
    init()
    create_table()
    #load_data(gen_data())
    #change_column()
    #read_data()
    thread_loaddata()
    #func1()