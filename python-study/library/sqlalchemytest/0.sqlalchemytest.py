#!usr/bin/env python
#coding:utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func


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

def test_func1():
    pass
    #print User.__table__
    #debug.printraw(dir(User)) 
    # 创建表
    Base.metadata.create_all(engine)

# 声明类有构造函数__init__，负责把关键字参数映射到定义的Column类属性里面去。
def test_func2():
    pass
    # 如果声明了没有的Column属性的关键字参数会报错。
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    #ed_user = User(name='ed', fullname='Ed Jones', password='edspassword', height="175")
    debug.printraw(ed_user.name)

Session = sessionmaker(bind=engine)
session = Session()

# 
def test_func3():
    pass
    # Session是一个类，在Python里，类也是一种对象。sessionmaker生成的只是类，
    # 相当于是设计院，只是把图纸生成出来了。
    #Session = sessionmaker(bind=engine)
    #session = Session()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    debug.trace(["ed_user.id:", ed_user.id])
    session.add(ed_user)
    debug.trace(["ed_user.id:", ed_user.id])
    # 在没有提交之前的查询都是在缓存在查询。
    our_user = session.query(User).filter_by(name='ed').first()  
    # 上面经过一个查询语句之后，ed_user.id就有值了。
    debug.trace(["ed_user.id:", ed_user.id])  
    #
    debug.printraw(our_user)
    debug.printraw(ed_user is our_user)
    # add_all函数添加多个对象
    debug.printraw(ed_user.id)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah'),
    ])
    #
    ed_user.password = 'f8s7ccs'
    #
    debug.printraw(ed_user.id)
    debug.printraw(session.dirty)
    debug.printraw(session.new)
    debug.printraw(ed_user.id)
    #
    session.commit()
    #debug.printraw(dir(session))
    

def test_func4():
    pass
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first() 
    debug.printraw(our_user)
    session.commit()
    ed_user.name = 'Edwardo'
    fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
    session.add(fake_user)
    #
    rv=session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
    debug.printraw(rv)
    #
    session.rollback()
    debug.trace(["ed_user.name:", ed_user.name])

def test_func41():
    pass
    # tmp是Query类的对象，Query对象实现了迭代器接口。
    tmp=session.query(User).order_by(User.id)
    #debug.printraw(tmp)
    #debug.trace(["type,str,dir:", type(tmp), tmp, dir(tmp)])
    for instance in tmp:
        debug.printraw([instance.name, instance.fullname])
    #
    for name, fullname in session.query(User.name, User.fullname):
        debug.printraw([name, fullname])
    # 
    for row in session.query(User, User.name).all():
        debug.printraw(row)
        # row的类型是sqlalchemy定义的命名Tuple，并不是Python系统内建的Tuple
        #debug.trace(["row:", row, type(row), dir(row)])

def func5():
    pass
    # 查询一个字段的方式，返回就是NamedTuple,直接查询User的方式返回的就是User对象。
    for row in session.query(User.name.label('name_label')).all():
    #for row in session.query(User).all():
        debug.trace(["row:", row, type(row), dir(row)])

def func6():
    pass
    user_alias = aliased(User, name='user_alias')
    for row in session.query(user_alias, user_alias.name).all():
        debug.trace(["row:", row, type(row)])

def func7():
    pass
    for u in session.query(User).order_by(User.id)[1:3]:
        debug.printraw(u)

def func8():
    pass
    # 这里name,的写法有点小技巧，name否面有个逗号，就变成了取每个元素里面的值了
    # filter_by函数的参数是使用关键字参数。
    for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
        debug.printraw(name)
    # 而filter函数的参数的形式是SQL表达式语言。不过感觉好奇怪。
    #tmp = (User.fullname=='Ed Jones')
    for name, in session.query(User.name).filter(User.fullname=='Ed Jones'):
        debug.printraw(name)

def func9():
    # 
    pass
    # Query对象全部是生成式的，意味着它的大部分方法调用返回的结果也是一个Query对象
    # 可以连环调用它的方法。这种方式有点像jQuery的写法。
    for user in session.query(User).filter(User.fullname=='ed').\
            filter(User.fullname=='Ed Jones'):
        debug.printraw(user)

# 过滤器操作符
def func10():
    pass
    session.query(User).filter(User.name=='ed')
    session.query(User).filter(User.name!='ed')
    session.query(User).filter(User.name.like('%ed%'))

# @note all, first, one, scalar的区别
# scalar返回的是元组的第一列。
def func11():
    pass
    rv1 = session.query(User).filter(User.name=='ed').all()
    rv2 = session.query(User).filter(User.name=='ed').first()
    rv3 = session.query(User).filter(User.id==16).one()
    rv4 = session.query(User, User.name, User.password).filter(User.id==20).scalar()  # scalar返回的是第一列
    rv5 = session.query(User, User.name, User.password).filter(User.id==20).first()    # first返回的是元组
    debug.printraw(rv1)
    debug.printraw(rv2)
    debug.printraw(rv3)
    debug.printraw(rv4)
    debug.printraw(rv5)

def func12():
    pass
    rv = session.query(User).filter(User.name.like('%ed%')).count()
    debug.printraw(rv)
    # func的类型是_FunctionGenerator
    #debug.trace(["trace:", dir(func), type(func)])
    #debug.trace(["trace:", dir(func), type(func.count)])
    debug.trace(["trace:", func.nasdaow23()])
    
#
if __name__ == "__main__":
    #test_func1()
    #test_func2()
    #test_func3()
    #test_func4()
    #func5()
    #func6()
    #func7()
    #func8()
    #func9()
    #func10()
    func11()
    #func12()
    
    