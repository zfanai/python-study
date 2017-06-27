#!usr/bin/env python
#coding:utf-8

#from __future__ import (absolute_import, unicode_literals)

"""
    Test Python function argument 
"""

# 隐式非关键字参数和隐式关键字参数是可变长参数，实参的形式是不固定的，长度也是可变的
# 类似于C语言里的可变参数func(a,b,...)

def DictArgDemo(a,b,c=3, *nokey_args, **key_args):
    print a,b,c
    print "nokey_args"
    for each_arg in nokey_args:
        print each_arg
    
    print "key_args"
    for each_arg in key_args:
        print each_arg

def func1():
    #DictArgDemo(c=5,b=6,a=7, 1, 2)  # 错误，实参在形式上，关键字参数不能出现在非关键字参数前面
    #DictArgDemo(5,6,7, 1, 2)  #正确, 前面3个是固定参数，后面两个是可变参数，只要是以非关键字形式给出的
                            # 都算到nokey_args里面去
    #DictArgDemo(c=5,a=6,b=7)  #正确，可变参数（非关键字和关键字）都没有
    #DictArgDemo(c=5,a=6,b=7,d=9)  #正确，非关键字可变参数没有
    #DictArgDemo(5,6,d=9)    # 正确， c使用了默认参数
    DictArgDemo(5,b=6,d=9)   # 正确

class DumpCls(object):    
    def dict_args_test(self, a, b, **params):
        print a,b,params
        
    def dict_args_call(self):
        options={u'call':12, u'kk':34, 'b':'de'}
        #self.dict_args_test('dd', **options)
        self.dict_args_test('dd', kk=34, call=12, b='de')
def func2():
    c=DumpCls()
    c.dict_args_call()
    
if __name__ == "__main__":
    #func1()
    func2()
    
    
    