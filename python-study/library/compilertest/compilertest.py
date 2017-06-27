#encoding:gbk

from distutils.msvc9compiler import MSVCCompiler

class Debug(object):
    def __init__(self):
        pass
    def trace(self, obj):
        print 'trace:', obj
debug=Debug()
c = MSVCCompiler()
c.initialize()

debug.trace(['c:',c])