#!usr/bin/env python
# -*- coding: utf-8 -*
import xlrd
import xlwt
import os
import datetime

class Debug(object):
    def trace(self, obj):
        print "trace:", obj
    def rprint(self, obj):
        print obj
debug = Debug()

# xlrd库是直接对文件进行操作，不通过COM接口
# 速度快。
# 也可以读取xlsx格式的Excel文件，文件扩展名并不是关键。
# 可能文件里面的2007格式的数据是关键。
def func1():
    wb=xlrd.open_workbook('test.xlsx')
    for s in wb.sheets():
        debug.trace(['Sheet:', s.name]) 
        for row in range(s.nrows):
            values=[]
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            debug.rprint(','.join(values))

# 写Excel文件测试
def func2():
    book=xlwt.Workbook()
    sheet1=book.add_sheet('Sheet l')
    book.add_sheet('Sheet 2')
    
    dt=datetime.datetime.now()
    sheet1.write(0,0,'A1')
    sheet1.write(0,1,'B1')
    row1=sheet1.row(1)
    row1.write(0, 'A2')
    row1.write(1, 'B2')
    sheet1.col(0).width=10000
    sheet1.row(2).set_cell_date(0, dt.time())
    #sheet1.row(2).write(0, '2015-12-21 16:06:23')
    
    sheet2=book.get_sheet(1)
    sheet2.row(0).write(0, 'Sheet 2 A1')
    sheet2.row(0).write(1, 'Sheet 2 B1')
    sheet2.flush_row_data()
    sheet2.write(1,0, 'Sheet 2 A3')
    sheet2.col(0).width=5000
    sheet2.col(0).hidden=True
    # 保存的是2003的格式。如果保存成xlsx会打开时显示文件格式不对。
    
    
    book.save(os.path.join(os.getcwd(), 'simple_%s.xls'%dt.strftime('%Y%m%d%H%M%S')))
    #book

if __name__ == '__main__':
    #func1()
    func2()
    #func3()
    #func31()
    #func4()
    #func5()
    #func6()
    
    