#encoding:gbk
import sys
from cStringIO import StringIO
import xhtml2pdf.pisa as pisa

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug = Debug()

def func1(html, pdf):
    #pdf = pisa.CreatePDF(open('test.html','rb'),open('test.pdf','wb'))
    pdf = pisa.CreatePDF(open(html,'rb'),open(pdf,'wb'))
    if not pdf.err:
        print "pdf is build"

if __name__=='__main__':
    if len(sys.argv)!=3:
        debug.trace('参数不正确。')
        sys.exit(1)
    #
    html = sys.argv[1]
    pdf = sys.argv[2]
    func1(html, pdf)