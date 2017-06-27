#encoding:gbk
'''
1.����е����͸ı�ʱ��ԭ�ȵ�ֵ����ת��Ϊ�µ�����ֵʱ
  ������Զ�������ת����������ܽ�������ת��Ϊ������
  ��ֵ����ᱨ�����ܽ��б�������޸ġ��������Ҫ��
  �б��������ת��ʱ������������Ҫ�ֶ�������������
  ת��
2.���ݿ������������ר��ϸ���Ϳ����������ݿ��һЩ
  ���ͼ��ȵȹ��ܣ������Ƴ����ͨ�ã����綼���ַ�
  ����ʾ���޸ķ��㣬���ǾͲ����������ݿ�����ͼ���
  ���ܡ����Բ������߼�á����е�������ǿ�������Ժ���
  �������ԵĲ�ͬ��ѧ��
2016-7-30 ͬһ��session������߳����û�����ú���������
���������һ����ÿ���̶߳������Լ���session��  
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
    # ���������йأ��������������Զ��ύ�������������
    # ���ÿ�β������ݿⶼ�����´����ӣ�ִ�����ٹر����ӵĻ��Ͳ�������Щ���⣬����
    # ��������Ч�ʱȽϵͣ���Ϊ���ݵĴ����ӣ��ر����Ӷ��ȽϺķ�ʱ�䡣
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

# String���û��ָ����С�Ļ�����MySQL��Ϊ�������ݿ�ʱ�ᱨ������ָ��
# �ַ����Ĵ�С��
class Tbl2(Base):
    __tablename__ = 'tbl2'
    id = Column(Integer, primary_key = True)
    day = Column(String(16))
    
# �����ͬ���߳�ʹ�ò�ͬ��session�ǿ��Գɹ��ġ�
# �������ͬһ�� session �����̷߳����ǻ�ʧ�ܵġ�        
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
        # session��commit�ǲ���д�����ݿ�ġ�
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

# ������Ȼ�ᱨ��������flask���������db.session�����Ե�ʱ��û�б���        
def load_data_t3(index):
    obj1=Tbl2(day='2015-07-21')
    session.add(obj1)
    session.commit()
    
# ���̷߳��ʻ�ʧ�ܡ�
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