# encoding:gbk
import os
import sys

class Debug(object):
    def trace(self, obj):
        print 'trace:', obj
debug=Debug()

# None对象小于所有的整数。
def func1():
    if None < 2.3:
        print 'None < 2.3'

    if None < -1:
        print 'None < -1'
        
    if None > 3.2:
        print 'None > 3.2'

    if None > -1:
        print 'None > -1'

def func2():
    # 为什么在项目里面null被翻译成null函数，而这里却是被当成了表示符。
    # 可能根据上下文的环境有关。
    #strobj=u'{"a":"中国", "b": null}'  
    strobj=u'{"a":"中国", "b": None}'   # None 是可识别的变量。
    debug.trace(['strobj:', strobj])
    exec "obj="+strobj
    debug.trace(['obj:', obj])

def func3():
    #print callable(getattr(, 'func2'))
    print __name__
    print sys.modules[__name__]
    cm=sys.modules[__name__]
    print callable(getattr(cm, 'func2'))

def func4(a, b):
    debug.trace(['func4 args:', a, b])
    
def func5():
    func4(1)

def createEmptyArray(dims=[]):
    #debug.trace(['========================dims', dims])
    dn=len(dims)
    #debug.trace(['dn', dn])
    if dn<1:return []
    #
    res=[]
    index=0
    while index<(dn):
        #debug.trace(['index:', index])
        size=dims[index]
        #
        while size>0:
            #debug.trace(['size:', size])
            res.append(createEmptyArray(dims[1:]))
            size=size-1
        #
        index=index+1
    return res

def func6():
    res=createEmptyArray([5, 2, 6])
    debug.trace(['res:', res])

def func7(data):
    data[0][1]=7

# @note 传递数组变量，在函数里面修改形参，会影响实参的值，也就是说
# 相当于是指针传递。
def func8():
    a=[[1,2]]
    func7(a)
    debug.trace(['a:', a])
    
def func9():
    print __line__

def func10():
    str1="http://fonts.googleapis.com/css?family=Roboto+Condensed2adsfa"
    str1=str1.replace("http://fonts.googleapis.com/css?family=Roboto+Condensed", '111')
    print str1

def func11():
    #s=":010205CD6BB20E1BE5"
    #s=":010201D02C"
    s=":0102020000FB"
    s1=map(lambda x:"%02X"%ord(x), s)
    debug.trace(["s1:", s1])
    s2=" ".join(s1)
    #
    '''s="32 30 31 36 2D 30 36 2D 31 37 20 31 33 3A 31 31"
    s1=s.split(" ")
    s2=map(lambda x:chr(int(x,16)),s1)
    s3="".join(s2)
    debug.trace(["s3:", s3])'''
    #
    fo=open("2.txt", "w")
    fo.write(s2)
    fo.close()
def func12():
    pass
    #中国=12   #py2不能用中文作为变量名，但是py3可以。
    #print 中国

# python对匿名函数的支持有限，只能写一个表达式。    
def func13():
    f=lambda x,y:x+y,x-=1
    f(1,2)
    
if __name__=='__main__':
    #func1()
    #func2()
    func13()
