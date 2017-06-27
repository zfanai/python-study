#encoding:gbk

import base
import pkgutil

class Debug(object):
    def trace(self,*msg):
        print 'trace:', msg
debug=Debug()

def func1():
    debug.trace('dir(pkgutil):', dir(pkgutil)) 
    loader=pkgutil.get_loader('_compat')
    debug.trace('loader:', loader) 
    __import__('_compat')
    

if __name__=='__main__':
    func1()