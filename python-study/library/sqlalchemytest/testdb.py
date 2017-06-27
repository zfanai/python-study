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