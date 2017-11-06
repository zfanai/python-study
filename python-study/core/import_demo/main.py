#!usr/bin/env python
# -*- coding: utf-8 -*

import sys
import Phone
import Phone.Mobile

#from History import HistoryAnalyzer
#from History import *
#import History

#from allattr import *
#from allattr import module1

#from History.HistoryAnalyzer import *
from History.HistoryAnalyzer import *



def func1():
    for module in Phone, Phone.Mobile, History:
        print dir(module)
        print module.__file__

def func2():
    #for module in Phone, Phone.Mobile, History:
    print dir(allattr)
    print allattr.__file__

#from Phone._internal import _height
import Phone._internal  # 这种方式可以

def func3():
    print Phone._internal._height
    Phone._internal._height=4
    print Phone._internal._height
    
    #print _height
    #_height=4    #出错
    m=__import__('History')
    print m.name
    
    import importlib
    try:
        m1=importlib.import_module('Phonex')
        print 'm1:', m1.abc
    except ImportError as e:
        print e

if __name__ == '__main__':
    #func1();
    #func2();
    #print dir()
    #print module1.name
    func3()
    