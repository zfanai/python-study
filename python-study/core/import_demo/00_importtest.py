#encoding:utf8

import sys

# 所有的导入都是相对于当前的解释器而言，所以对于已经导入过的模块
# 再次导入不会触发模块的全局代码再次执行。
import module2  
import module3

import module2

class Debug(object):
    def trace(self,msg):
        print 'trace:', msg
debug=Debug()

def func1():
    module2.func1()
    module3.func1()

if __name__ == '__main__':
    func1()
    