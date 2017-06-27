#encoding:gbk


import win32com.client
import sys
from datetime import *

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
    def rprint(self, msg):
        print msg
debug=Debug()

convertFactor=1.0
timeOffset=False

class XlsProxy(object):
    def __init__(self, xlsfile):
        xlApp = win32com.client.Dispatch("Excel.Application")
        #filename = os.path.join(os.getcwd(), sys.argv[1])  
        #fontFileName = os.path.join(os.getcwd(), sys.argv[2]) 
        self.book = xlApp.Workbooks.open(xlsfile)
        self.sheet = self.book.Sheets(1)
        
    def setSheet(self, n):
        self.sheet=self.book.Sheets(n)
        
    def readCell(self, row, col):
        return self.sheet.Cells(row, col).Value
    
    def close(self):
        self.book.Close()
    
    def getUserRane(self):
        nMaxCol=0
        nMaxRow = self.sheet.UsedRange.Rows.Count
        nMaxCol = self.sheet.UsedRange.Columns.Count
        #debug.rprint(dir(self.sheet.UsedRange.Rows))
        #
        
        return nMaxRow, nMaxCol
        

def readXls(xlsfile):
    debug.trace(['xlsfile:', xlsfile])
    proxy=XlsProxy(xlsfile)
    tmp=proxy.readCell(1,1)
    debug.trace(['tmp:', tmp])
    tmp=proxy.getUserRane()
    debug.trace(['tmp:', tmp])
    #
    #nMaxRow=10
    n=datetime.now()
    st=n-timedelta(days=6)
    debug.trace(['st:', st])
    #
    c1=proxy.readCell(2, 1)
    sts=int(c1)
    pst=datetime.fromtimestamp(sts)
    #st.replace(hour=pst.hour, minute=pst.minute, second=0, microsecond=0)
    st=datetime(st.year, st.month, st.day, pst.hour, pst.minute)
    debug.trace(['pst,st:', pst, st])
    #
    data=[]
    #nMaxRow=100
    #for row in range(2, nMaxRow):
    row=2
    while True:
        # 
        c1=proxy.readCell(row, 1)
        c2=proxy.readCell(row, 2)
        #c3=proxy.readCell(row, 3)
        if not c1:break
        #
        #debug.trace(['c1,c2,c3:', c1, c2, c3])
        #debug.trace(['c1,c2,c3:', int(c1), c2, c3, type(c1), type(c2), type(c3)])
        if row%100==0:
            debug.trace(['row:', row])
        #
        if timeOffset:
            oft=int(c1)-sts
            dt=st+timedelta(seconds=oft)
        else:
            dt=datetime.fromtimestamp(int(c1))
        
        #
        #dt=datetime.fromtimestamp(int(c1))
        dts=dt.strftime('%Y-%m-%d %H:%M:%S')
        data.append([dts, round(c2/convertFactor, 4)])
        #debug.trace(['dts:', dts, c2/18.0])
        row += 1
    #    
    debug.trace(['row:', row])    
    #
    proxy.close()
    
    # 根据第一个元素的时间来
    start_time=datetime.strptime(data[0][0], '%Y-%m-%d %H:%M:%S')
    size=len(data)
    for i in range(size):
        item=data[i]
        dt=start_time+timedelta(minutes=i*2)
        item[0]=dt.strftime('%Y-%m-%d %H:%M:%S')
    #
    return data

def saveToFile(data, file):
    fo=open(file, 'w')
    for item in data:
        #debug.trace(['item:', item])
        str='%s,%.4f\n' % (item[0], item[1])
        fo.write(str)
    fo.close()
#
if __name__=='__main__':
    xlsfile=sys.argv[1]
    #nMaxRow=int(sys.argv[2])
    of=sys.argv[2]
    #pwd=sys.argv[3]
    #db=sys.argv[4]
    #
    data=readXls(xlsfile)
    saveToFile(data, of)
    