#encoding:gbk

'''
subprocess���µ�Python�汾�Ƽ�ʹ�õ�ģ�顣
'''

import subprocess

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    args=['notepad', '1.txt']
    p=subprocess.Popen(args)
    debug.trace(['p:', p])
    
if __name__=='__main__':
    func1()