#encoding:gbk

"""
1. _xx��ʽ�ı������ܵ���, from m1 import *  Ĭ���ǲ�����ģ����û����ȷָ��__all__�����Ļ���
2. __xx��ʽ�ı���ϵͳ�����һ��ǰ׺_cls(�ⲿ���ʵ�ʱ��)
3. __xx__��ʽ�ı�����Ȼ���Խ��飬���Ǳ�̹淶��Ӧ��������������Ϊϵͳ��һ���������������
�����ģ��������������
"""

from m1 import *
from m1 import car


class Debug(object):
    def trace(self,msg):
        print 'trace:',msg
debug=Debug()

debug.trace(['car._color:', car._color]) 
class Dog(object):
    def __init__(self):
        self.__x=1
        self.__y__=1
    def _run(self):
        debug.trace('_run')
        print '__y__:', self.__y__

def func1():
    d=Dog()
    #debug.trace(['d.__x:', d.__x])
    d._run()
    #debug.trace(['_VER:', _VER])
    debug.trace(['VER:', VER])
    #debug.trace(['NAME:', _NAME])
    debug.trace(['car:', car])
    
if __name__ == '__main__':
    func1()
    


