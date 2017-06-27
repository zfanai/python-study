#encoding:gbk
import os
import argparse

class Debug(object):
    def trace(self, *msg):print 'trace:', msg
debug=Debug()

# NOTE：170307
# 位置参数和可选参数的概念
# 位置参数就是约定出现在第几个位置上的参数。可选参数类似于-h 或 --help这样的形式的参数。
# 1. 使用argparse的好处之一就是得到一个规范统一的帮助信息，当输入的参数不对时，会给出帮助信息。

def func1():
    parse=argparse.ArgumentParser(usage='ddd')
    parse.add_argument('echo', help='echo the string you use here')
    ns,remaining_args=parse.parse_known_args()
    debug.trace('ns:', ns, remaining_args)

# 这个是帮助文档里面的示例代码。
def func2():
    #import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    # metavar='N'相当于就一下子定义了多个位置参数， 相当于python里面的列表参数。
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')
    
    args = parser.parse_args()
    print args.accumulate(args.integers)

# add_argument的会识别输入的参数的名称还是的标志（flag, 也就是可选参数, 这里的可选参数需要在搭配一个参数，类似于python的字典参数）
# 但是这种可选参数跟ls -al 这样的可选参数要求不同， ls -al的可选参数的-al 后面不用跟一个搭配的参数。这种行为跟action参数的设置有关。
# 如果可选参数是一个字母，多个一个字母的可选参数可以合并到一起写。也就是-d -j 可以写成 -dj
def func3():
    parser = argparse.ArgumentParser(description='Study argparse module.')
    parser.add_argument('-jx', '-f', action='store_const', const=42)
    parser.add_argument('-dx', action='store_const', const=42)
    parser.add_argument('bar')
    #args = parser.parse_args()
    args = parser.parse_known_args()
    print 'args:', args
    
if __name__=='__main__':
    func3()