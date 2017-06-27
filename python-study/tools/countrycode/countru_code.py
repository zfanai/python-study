#encoding:gbk
import xlrd
from zftrace import debug

def func1():
    wb=xlrd.open_workbook('国际短信资费表.xls')
    #for s in wb.sheets():
    #    debug.trace('app', 'Sheet:', s.name) 
    '''
    for row in range(s.nrows):
        values=[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        debug.rprint(','.join(values))'''
    s=wb.sheets()[0]
    data=[]
    for row in range(1, s.nrows):
        values=[]
        for col in range(s.ncols):
            v=s.cell(row,col).value
            values.append(v.encode('gbk') if isinstance(v,unicode) else v)
        #print  values
        #debug.trace('app', ','.join(values))   
        #print values
        data.append(values)
    # 
    #print type(data[0][0].encode('gbk'))
    #print data[0][1].encode('gbk')
    str_data=[]
    
    '''for x in data:
        x=map(lambda e:e.encode('gbk') if isinstance(e,unicode) else e, x)
        b=x[1]
        print x[0]
        print "'%s',%s"%(x[0], b)
        #str_data.append("('%s', '%s', '%s', %s)"%(x[0], b, x[2],x[3]) )'''
    str_data=map(lambda x:"('%s','%s','%s',%s)"%(x[0],x[1],x[2],int(x[3])), data)
    #print str_data[0:3]
    str_data=','.join(str_data)
    print str_data[0:300]
    strsql='''insert into country_code (code,zh_name,en_name,zip) values %s; ''' % str_data  
    with open('output.sql', 'w') as f:
        f.write(strsql)

if __name__=='__main__':
    func1()