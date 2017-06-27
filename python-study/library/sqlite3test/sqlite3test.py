#encoding:gbk
import sqlite3

class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def printraw(self, obj):
        print obj
#
debug = Debug()


def func1():
    conn=sqlite3.connect('JN011Test.db')
    c=conn.cursor()
    
    c.execute('select id from jn011test_session;')
    #debug.trace(c.fetchone())
    #num=c.rowcount
    #debug.trace(c.rowcount)
    #debug.trace(dir(c))
    rv=c.fetchall()
    #debug.trace(rv)
    
    for row in rv:
        c.execute('select sid,count(*) from jn011test_data where sid=?;', row)
        rv2=c.fetchall()
        #debug.trace(rv2)
        sid,data_num=rv2[0][:]
        if not data_num:continue
        c.execute('select distinct(injectNo)from jn011test_data where sid=?;', [(sid)]);
        rv3=c.fetchall()
        size=len(rv3)
        
        debug.trace("\r\n=======================")
        debug.trace(["sid,data_num:", sid, data_num])
        for i in range(1,size):
            cur_no,prev_no=rv3[i][0],rv3[i-1][0]
            if cur_no-prev_no!=1:debug.trace([prev_no, cur_no, cur_no-prev_no])
    
    conn.commit()
    conn.close()

if __name__=='__main__':
    func1()