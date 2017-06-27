#encoding:gbk

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func
from datetime import *
import sys

class Debug(object):
    def trace(self, obj):
        print "trace:", obj

debug = Debug()

#

session=None
def init(pwd, db):
    global session
    #
    #engine = create_engine('mysql://root:myzfsql85@localhost/sqlalchemytest', echo=False)
    engine = create_engine('mysql://root:%s@localhost/%s' % (pwd, db), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

def func1():
    strsql='select * from personal_info;'
    #strsql='select * from user;'
    res=session.execute(strsql)
    num=res.rowcount
    debug.trace(['num:', num])
    data=[]
    for i in range(0,num):
        row=res.fetchone()
        debug.trace(['row:', row['id'], row['birth_date']])
        data.append({'id':row['id'], 'birth_date':row['birth_date'] })
    #
    return data

def func2():
    strsql='alter table personal_info modify birth_date date;'
    res=session.execute(strsql)
    strsql='alter table diabetes_info modify confirm_time date;'
    res=session.execute(strsql)
    strsql='alter table upload_record change type devicetype varchar(8);'
    res=session.execute(strsql)
    #UploadRecord devicetype
    session.commit()

# @zfn string 转 date 是自动转化的吗。
def func3(data):
    for item in data:
        birth_date=item['birth_date']
        if birth_date is None:
            continue
        d=datetime.strptime(birth_date, '%Y-%m-%s')
        d=d.date()
        
if __name__=='__main__':
    if len(sys.argv)!=3:
        debug.trace('args not right.')
        sys.exit(1)
    #
    pwd=sys.argv[1]
    db=sys.argv[2]
    #
    init(pwd, db)
    #data=func1()
    func2()