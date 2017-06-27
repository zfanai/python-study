#encoding:gbk

import sys

# 系统默认的字符编码是ascii, 而文件第一行声明的编码只是文件的编码方式。
# a在隐式的编码转换处理过程中， 采用的就是默认的字符编码来解码， 也就是用ascii来解码， 
# 但是用ascii来解码中文字串就会报错， 因为ascii编码不支持中文。

a='上周六'
b=u'上周六'   # 这个是字面量， 所以在编译源码的过程中， 就采用文件编码方式的编码把字串解码成Unicode对象。

#print b

print a==b
print sys.getdefaultencoding()