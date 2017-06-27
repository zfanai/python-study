#encoding:utf8

import sys
print sys.getdefaultencoding()
#reload(sys)    # 不写这一行就无法调用setdefaultencoding属性。
#sys.setdefaultencoding('utf8')
#sys.setdefaultencoding('ascii')
#sys.setdefaultencoding('gbk')
print sys.getdefaultencoding()

a='上周六'
b=u'上周六'
print type(a),type(b)
print a==b

#print sys.getdefaultencoding()
c='234'
d=u'234'
print c==d