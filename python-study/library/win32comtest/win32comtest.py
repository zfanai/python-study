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
       
def saveToFile(data, file):
    fo=open(file, 'w')
    for item in data:
        str='%s,%.2f\n' % (item[0], item[1])
        fo.write(str)
    fo.close()
#
def func1():
    xlApp = win32com.client.Dispatch("Excel.Application")
    debug.trace(['xlApp:', xlApp])

def func2():
    xlsfile=sys.argv[1]
    nMaxRow=int(sys.argv[2])
    of=sys.argv[3]
    #pwd=sys.argv[3]
    #db=sys.argv[4]
    
    data=readXls(xlsfile, nMaxRow)
    saveToFile(data, of)
#
if __name__=='__main__':
    func2()
    