#encoding:gbk

# NOTE: zhouf, 170315, __future__���������뽫���ƻ������һЩ���ԡ�����ƽ̨���ϰ汾������ʹ��δ���°汾��һЩ���ԡ�
#  ����һ�������ݵ�д����
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
    
