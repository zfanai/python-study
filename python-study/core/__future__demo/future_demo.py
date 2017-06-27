#encoding:gbk

# NOTE: zhouf, 170315, __future__包可以引入将来计划引入的一些特性。运行平台是老版本，但是使用未来新版本的一些特性。
#  这是一种向后兼容的写法。
from __future__ import unicode_literals
import datetime


class Debug(object):
    def trace(self,msg):
        nt=datetime.datetime.now()
        print "[%s]:%s" % (nt.strftime('%Y%m%d%H%M%S'), msg)
debug = Debug()

def func1():
    print '\'xxx\' is unicode?', isinstance('xxx', unicode)
    print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
    print '\'xxx\' is str?', isinstance('xxx', str)
    print 'b\'xxx\' is str?', isinstance(b'xxx', str)
    
if __name__ == "__main__":
    func1()
    
