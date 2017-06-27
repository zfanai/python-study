#encoding:gbk
import os
import argparse

class Debug(object):
    def trace(self, *msg):print 'trace:', msg
debug=Debug()

# NOTE��170307
# λ�ò����Ϳ�ѡ�����ĸ���
# λ�ò�������Լ�������ڵڼ���λ���ϵĲ�������ѡ����������-h �� --help��������ʽ�Ĳ�����
# 1. ʹ��argparse�ĺô�֮һ���ǵõ�һ���淶ͳһ�İ�����Ϣ��������Ĳ�������ʱ�������������Ϣ��

def func1():
    parse=argparse.ArgumentParser(usage='ddd')
    parse.add_argument('echo', help='echo the string you use here')
    ns,remaining_args=parse.parse_known_args()
    debug.trace('ns:', ns, remaining_args)

# ����ǰ����ĵ������ʾ�����롣
def func2():
    #import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    # metavar='N'�൱�ھ�һ���Ӷ����˶��λ�ò����� �൱��python������б������
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')
    
    args = parser.parse_args()
    print args.accumulate(args.integers)

# add_argument�Ļ�ʶ������Ĳ��������ƻ��ǵı�־��flag, Ҳ���ǿ�ѡ����, ����Ŀ�ѡ������Ҫ�ڴ���һ��������������python���ֵ������
# �������ֿ�ѡ������ls -al �����Ŀ�ѡ����Ҫ��ͬ�� ls -al�Ŀ�ѡ������-al ���治�ø�һ������Ĳ�����������Ϊ��action�����������йء�
# �����ѡ������һ����ĸ�����һ����ĸ�Ŀ�ѡ�������Ժϲ���һ��д��Ҳ����-d -j ����д�� -dj
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