#encoding:gbk

from sqlalchemy import *
# engine����Ҳ����ֱ��ִ��sql����
def func1():
    engine = create_engine('mysql://root:myzfsql85@localhost/test')
    connection=engine.connect()
    result = connection.execute('select login from users')
    for row in result:
        print "username:", row['login']
    connection.close()

def func2():
    engine = create_engine('mysql://root:myzfsql85@localhost/test')
    result = engine.execute('select login from users')
    for row in result:
        print "username:", row['login']
def func3():
    # ֱ��д�����ݿ⣬����Ҫ commit
    engine = create_engine('mysql://root:myzfsql85@localhost/test')
    result = engine.execute('insert into users (login,uid,prid) values ("aaa", 1, 2)')
    #for row in result:
    #    print "username:", row['login']
        
if __name__=='__main__':
    func3()