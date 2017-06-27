#encoding:gbk

'''
2016-8-1 repr是对Python友好的，str是对用户友好的。
'''

class Debug(object):
    def trace(self, msg):print 'trace:', msg
debug=Debug()

class Dog(object):
    pass
    def __repr__(self):return 'repr dog'
    def __str__(self):return 'str dog'
def func1():
    d=Dog()
    str_repr=repr(d)
    str_str=str(d)
    debug.trace(str_repr)
    debug.trace(str_str)
    #eval('a=123')
    exec('a=123')
    print a
    print `d`   # `xx` 表示调用repr(xx)

def func2():
    debug.trace(repr([1,2,3]))
    debug.trace(str([1,2,3]))

if __name__=='__main__':
    func1()
    #func2()