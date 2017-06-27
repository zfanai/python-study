#!usr/bin/env python
#coding:utf-8

"""
    Test Python function argument 
    默认参数不一定要放在前面。
    函数的定义来说，参数类型的排列依次是：
    位置参数,关键字参数(默认参数),
    隐式非关键字参数，隐式关键字参数
    
    参数从是否明确列出来的角度可分为两类：
    1.显式参数（指定了形参的名称）
    2.隐式参数（没有指定形参的名称）
    前面两个，位置参数,关键字参数(默认参数)称为
    显式参数。后面两个称为隐式参数。
    
"""

def ArgsTest(a,b,c=None):
    print a,b
    print c

#def ArgsTest1(b=2, a, c=None):    # 默认参数不能在位置参数前面 
def ArgsTest1(a,b=2,c=None):
    print a,b
    print c
    
if __name__ == "__main__":
    ArgsTest(1,2)
    
    # 
    #ArgsTest1(2, b=5,c=3)  #正确
    #ArgsTest1(a=4, 5, c=3)  #错误，在调用上非关键字参数，不能再关键字参数的前边
    #ArgsTest1(b=4, a=5, c=3) # 正确，定义的非默认形参
    #ArgsTest1(b=4, c=5) # 错误，位置参数a要么在前面，要么通过关键字参数给出
    ArgsTest1(b=4, a=5) # 正确，只要位置参数能给正确满足，默认参数就不是问题了
    